"""Run with: blender -b D1_LAYOUT_PREVIEW.blend --python scripts/inspect_blend.py
Exports coarse model stats; these do NOT certify visual quality.
"""
import bpy, json, os, math
from mathutils import Vector


def vertices_bbox(objs):
    coords=[]
    for o in objs:
        if o.type not in {'MESH','CURVE'}: continue
        coords.extend([o.matrix_world @ Vector(c) for c in o.bound_box])
    if not coords: return None
    lo=[min(c[i] for c in coords) for i in range(3)]
    hi=[max(c[i] for c in coords) for i in range(3)]
    return {"min":lo,"max":hi,"extent":[hi[i]-lo[i] for i in range(3)]}

result={"file":bpy.data.filepath,"blender":bpy.app.version_string,"scenes":{},"characters":{}}
for sc in bpy.data.scenes:
    result['scenes'][sc.name]={"engine":sc.render.engine,"width":sc.render.resolution_x,"height":sc.render.resolution_y,"fps":sc.render.fps,"camera":sc.camera.name if sc.camera else None}
for col in bpy.data.collections:
    if not col.name.startswith('CHAR_'):continue
    objs=list(col.objects)
    mesh=[o for o in objs if o.type=='MESH']
    report={"objects":len(objs),"mesh_objects":len(mesh),"vertices":sum(len(o.data.vertices) for o in mesh),"polygons":sum(len(o.data.polygons) for o in mesh),"mesh_with_uv":sum(bool(o.data.uv_layers) for o in mesh),"mesh_with_shape_keys":sum(bool(o.data.shape_keys) for o in mesh),"armature_objects":sum(o.type=='ARMATURE' for o in objs),"subdivision_modifiers":sum(m.type=='SUBSURF' for o in objs for m in o.modifiers),"mesh_bounds_local_reference":vertices_bbox(objs)}
    result['characters'][col.name]=report
output=os.environ.get('PINOCCHIO_BLEND_AUDIT_JSON','/tmp/pinocchio_blend_audit.json')
with open(output,'w',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False,indent=2))
print('Wrote',output)
