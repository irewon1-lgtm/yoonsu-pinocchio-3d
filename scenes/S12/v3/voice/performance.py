"""Bind the approved S12 acting intent to native IndexTTS2 emotion controls."""

# The engine's eight axes are happy, angry, sad, afraid, disgusted,
# melancholic, surprised, and calm. No unrecognized settings or pitch/rate edits.
PALETTE = {
    'wonder':  (.245,.018,.013,.060,.151,.300),
    'welcome': (.283,.016,.009,.049,.095,.330),
    'inquiry': (.205,.021,.019,.070,.108,.365),
    'settled': (.208,.020,.014,.051,.062,.430),
    'breeze':  (.219,.017,.018,.071,.165,.283),
    'tension': (.081,.035,.098,.090,.264,.210),
    'alarm':   (.067,.031,.272,.041,.274,.085),
    'blocked': (.056,.100,.235,.059,.141,.186),
    'concern': (.135,.056,.108,.090,.117,.277),
    'urgent':  (.104,.041,.235,.053,.192,.148),
    'resolve': (.159,.039,.077,.080,.037,.398),
    'trust':   (.220,.026,.026,.077,.063,.375),
    'relief':  (.375,.025,.038,.069,.124,.152),
    'joy':     (.491,.012,.022,.040,.160,.067),
    'awe':     (.330,.024,.040,.099,.238,.049),
    'embrace': (.294,.067,.023,.093,.091,.216),
    'truth':   (.124,.123,.082,.109,.051,.290),
    'hope':    (.246,.029,.018,.108,.067,.310),
    'proud':   (.323,.034,.018,.078,.095,.233),
    'farewell':(.242,.067,.012,.128,.065,.270),
    'closing': (.179,.033,.008,.118,.035,.412),
    'model':   (.183,.013,.010,.065,.054,.456),
}

# Each value follows the corresponding V3 emotion_target and direction_en.
NARRATIVE = {
    'U001':'welcome', 'U002':'tension', 'U003':'alarm', 'U004':'blocked',
    'U005':'concern', 'U006':'blocked', 'U007':'urgent', 'U008':'resolve',
    'U009':'trust', 'U010':'concern', 'U011':'relief', 'U012':'joy',
    'U013':'settled', 'U014':'embrace', 'U015':'proud', 'U016':'resolve',
    'U017':'wonder', 'U018':'embrace', 'U019':'resolve', 'U020':'trust',
    'U021':'settled', 'U022':'proud', 'U023':'settled', 'U024':'embrace',
    'U025':'trust', 'U026':'wonder', 'U027':'awe', 'U028':'awe',
    'U029':'joy', 'U030':'awe', 'U031':'embrace', 'U032':'awe',
    'U033':'proud', 'U034':'hope', 'U035':'relief', 'U036':'farewell',
    'U037':'hope', 'U038':'settled', 'U039':'wonder', 'U040':'resolve',
    'U041':'settled', 'U042':'hope', 'U043':'farewell', 'U044':'closing',
    'N001':'welcome', 'N002':'inquiry', 'N003':'wonder', 'N004':'trust',
    'N005':'breeze', 'N006':'inquiry', 'N007':'relief', 'N008':'concern',
    'N009':'truth', 'N010':'embrace', 'N011':'concern', 'N012':'relief',
    'N013':'inquiry', 'N014':'settled', 'N015':'wonder', 'N016':'inquiry',
    'N017':'embrace', 'N018':'wonder', 'N019':'awe', 'N020':'embrace',
    'N021':'settled', 'N022':'trust', 'N023':'embrace', 'N024':'relief',
    'N025':'welcome', 'N026':'hope', 'N027':'farewell',
}

# Explicit emotional turns use only the script's existing clause/beat boundaries.
TURNS = {
    'U003': ('Oh!', 90, 'breeze'),
    'U005': ('Cricket!', 116, 'alarm'),
    'U006': ("I'm okay,", 118, 'trust'),
    'U029': ('Grandpa!', 116, 'awe'),
    'U031': ('Pinocchio!', 134, 'awe'),
    'U035': ('I will.', 105, 'resolve'),
    'N009': ('Yes.', 141, 'settled'),
    'N012': ("I'm not hurt.", 109, 'trust'),
    'N026': ('There.', 108, 'settled'),
}


def vector(preset):
    happy, sad, afraid, melancholic, surprised, calm = PALETTE[preset]
    result = [happy, 0., sad, afraid, 0., melancholic, surprised, calm]
    assert all(0 <= weight <= .8 for weight in result) and sum(result) <= .800001
    return result


def beats(cue, text):
    code = cue.split('-')[1]
    final = 'model' if code.startswith('M') else NARRATIVE[code]
    if code in TURNS:
        head, pause, initial = TURNS[code]
        assert text.startswith(head + ' ')
        tail = text[len(head)+1:]
        return [{'text': head, 'vector': vector(initial), 'pause_ms': pause, 'intent': initial},
                {'text': tail, 'vector': vector(final), 'pause_ms': 0, 'intent': final}]
    return [{'text': text, 'vector': vector(final), 'pause_ms': 0, 'intent': final}]
