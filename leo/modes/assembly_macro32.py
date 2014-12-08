# Leo colorizer control file for assembly_macro32 mode.
# This file is in the public domain.

# Properties for assembly_macro32 mode.
properties = {
	"lineComment": ";",
}

# Attributes dict for assembly_macro32_main ruleset.
assembly_macro32_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"escape": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for assembly_macro32 mode.
attributesDictDict = {
	"assembly_macro32_main": assembly_macro32_main_attributes_dict,
}

# Keywords dict for assembly_macro32_main ruleset.
assembly_macro32_main_keywords_dict = {
	".address": "keyword1",
	".align": "keyword1",
	".ascic": "keyword1",
	".ascid": "keyword1",
	".ascii": "keyword1",
	".asciz": "keyword1",
	".blka": "keyword1",
	".blkb": "keyword1",
	".blkd": "keyword1",
	".blkf": "keyword1",
	".blkg": "keyword1",
	".blkh": "keyword1",
	".blkl": "keyword1",
	".blko": "keyword1",
	".blkq": "keyword1",
	".blkw": "keyword1",
	".byte": "keyword1",
	".cross": "keyword1",
	".d_floating": "keyword1",
	".debug": "keyword1",
	".default": "keyword1",
	".disable": "keyword1",
	".double": "keyword1",
	".dsabl": "keyword1",
	".enabl": "keyword1",
	".enable": "keyword1",
	".end": "keyword1",
	".endc": "keyword1",
	".endm": "keyword1",
	".endr": "keyword1",
	".entry": "keyword1",
	".error": "keyword1",
	".even": "keyword1",
	".external": "keyword1",
	".extrn": "keyword1",
	".f_floating": "keyword1",
	".float": "keyword1",
	".g_floating": "keyword1",
	".global": "keyword1",
	".globl": "keyword1",
	".h_floating": "keyword1",
	".ident": "keyword1",
	".if": "keyword1",
	".if_false": "keyword1",
	".if_true": "keyword1",
	".if_true_false": "keyword1",
	".iff": "keyword1",
	".ift": "keyword1",
	".iftf": "keyword1",
	".iif": "keyword1",
	".irp": "keyword1",
	".irpc": "keyword1",
	".library": "keyword1",
	".link": "keyword1",
	".list": "keyword1",
	".long": "keyword1",
	".macro": "keyword1",
	".mask": "keyword1",
	".mcall": "keyword1",
	".mdelete": "keyword1",
	".mexit": "keyword1",
	".narg": "keyword1",
	".nchr": "keyword1",
	".nlist": "keyword1",
	".nocross": "keyword1",
	".noshow": "keyword1",
	".ntype": "keyword1",
	".octa": "keyword1",
	".odd": "keyword1",
	".opdef": "keyword1",
	".packed": "keyword1",
	".page": "keyword1",
	".print": "keyword1",
	".psect": "keyword1",
	".quad": "keyword1",
	".ref1": "keyword1",
	".ref16": "keyword1",
	".ref2": "keyword1",
	".ref4": "keyword1",
	".ref8": "keyword1",
	".repeat": "keyword1",
	".rept": "keyword1",
	".restore": "keyword1",
	".restore_psect": "keyword1",
	".save": "keyword1",
	".save_psect": "keyword1",
	".sbttl": "keyword1",
	".show": "keyword1",
	".signed_byte": "keyword1",
	".signed_word": "keyword1",
	".subtitle": "keyword1",
	".title": "keyword1",
	".transfer": "keyword1",
	".warn": "keyword1",
	".weak": "keyword1",
	".word": "keyword1",
	"acbb": "function",
	"acbd": "function",
	"acbf": "function",
	"acbg": "function",
	"acbh": "function",
	"acbl": "function",
	"acbw": "function",
	"adawi": "function",
	"addb2": "function",
	"addb3": "function",
	"addd2": "function",
	"addd3": "function",
	"addf2": "function",
	"addf3": "function",
	"addg2": "function",
	"addg3": "function",
	"addh2": "function",
	"addh3": "function",
	"addl2": "function",
	"addl3": "function",
	"addp4": "function",
	"addp6": "function",
	"addw2": "function",
	"addw3": "function",
	"adwc": "function",
	"aobleq": "function",
	"aoblss": "function",
	"ap": "keyword3",
	"ashl": "function",
	"ashp": "function",
	"ashq": "function",
	"bbc": "function",
	"bbcc": "function",
	"bbcci": "function",
	"bbcs": "function",
	"bbs": "function",
	"bbsc": "function",
	"bbss": "function",
	"bbssi": "function",
	"bcc": "function",
	"bcs": "function",
	"beql": "function",
	"beqlu": "function",
	"bgeq": "function",
	"bgequ": "function",
	"bgtr": "function",
	"bgtru": "function",
	"bicb2": "function",
	"bicb3": "function",
	"bicl2": "function",
	"bicl3": "function",
	"bicpsw": "function",
	"bicw2": "function",
	"bicw3": "function",
	"bisb2": "function",
	"bisb3": "function",
	"bisl2": "function",
	"bisl3": "function",
	"bispsw": "function",
	"bisw2": "function",
	"bisw3": "function",
	"bitb": "function",
	"bitl": "function",
	"bitw": "function",
	"blbc": "function",
	"blbs": "function",
	"bleq": "function",
	"blequ": "function",
	"blss": "function",
	"blssu": "function",
	"bneq": "function",
	"bnequ": "function",
	"bpt": "function",
	"brb": "function",
	"brw": "function",
	"bsbb": "function",
	"bsbw": "function",
	"bvc": "function",
	"bvs": "function",
	"callg": "function",
	"calls": "function",
	"caseb": "function",
	"casel": "function",
	"casew": "function",
	"chme": "function",
	"chmk": "function",
	"chms": "function",
	"chmu": "function",
	"clrb": "function",
	"clrd": "function",
	"clrf": "function",
	"clrg": "function",
	"clrh": "function",
	"clrl": "function",
	"clro": "function",
	"clrq": "function",
	"clrw": "function",
	"cmpb": "function",
	"cmpc3": "function",
	"cmpc5": "function",
	"cmpd": "function",
	"cmpf": "function",
	"cmpg": "function",
	"cmph": "function",
	"cmpl": "function",
	"cmpp3": "function",
	"cmpp4": "function",
	"cmpv": "function",
	"cmpw": "function",
	"cmpzv": "function",
	"crc": "function",
	"cvtbd": "function",
	"cvtbf": "function",
	"cvtbg": "function",
	"cvtbh": "function",
	"cvtbl": "function",
	"cvtbw": "function",
	"cvtdb": "function",
	"cvtdf": "function",
	"cvtdh": "function",
	"cvtdl": "function",
	"cvtdw": "function",
	"cvtfb": "function",
	"cvtfd": "function",
	"cvtfg": "function",
	"cvtfh": "function",
	"cvtfl": "function",
	"cvtfw": "function",
	"cvtgb": "function",
	"cvtgf": "function",
	"cvtgh": "function",
	"cvtgl": "function",
	"cvtgw": "function",
	"cvthb": "function",
	"cvthd": "function",
	"cvthf": "function",
	"cvthg": "function",
	"cvthl": "function",
	"cvthw": "function",
	"cvtlb": "function",
	"cvtld": "function",
	"cvtlf": "function",
	"cvtlg": "function",
	"cvtlh": "function",
	"cvtlp": "function",
	"cvtlw": "function",
	"cvtpl": "function",
	"cvtps": "function",
	"cvtpt": "function",
	"cvtrdl": "function",
	"cvtrfl": "function",
	"cvtrgl": "function",
	"cvtrhl": "function",
	"cvtsp": "function",
	"cvttp": "function",
	"cvtwb": "function",
	"cvtwd": "function",
	"cvtwf": "function",
	"cvtwg": "function",
	"cvtwh": "function",
	"cvtwl": "function",
	"decb": "function",
	"decl": "function",
	"decw": "function",
	"divb2": "function",
	"divb3": "function",
	"divd2": "function",
	"divd3": "function",
	"divf2": "function",
	"divf3": "function",
	"divg2": "function",
	"divg3": "function",
	"divh2": "function",
	"divh3": "function",
	"divl2": "function",
	"divl3": "function",
	"divp": "function",
	"divw2": "function",
	"divw3": "function",
	"editpc": "function",
	"ediv": "function",
	"emodd": "function",
	"emodf": "function",
	"emodg": "function",
	"emodh": "function",
	"emul": "function",
	"extv": "function",
	"extzv": "function",
	"ffc": "function",
	"ffs": "function",
	"fp": "keyword3",
	"halt": "function",
	"incb": "function",
	"incl": "function",
	"incw": "function",
	"index": "function",
	"insqhi": "function",
	"insqti": "function",
	"insque": "function",
	"insv": "function",
	"iota": "function",
	"jmp": "function",
	"jsb": "function",
	"ldpctx": "function",
	"locc": "function",
	"matchc": "function",
	"mcomb": "function",
	"mcoml": "function",
	"mcomw": "function",
	"mfpr": "function",
	"mfvp": "function",
	"mnegb": "function",
	"mnegd": "function",
	"mnegf": "function",
	"mnegg": "function",
	"mnegh": "function",
	"mnegl": "function",
	"mnegw": "function",
	"movab": "function",
	"movad": "function",
	"movaf": "function",
	"movag": "function",
	"movah": "function",
	"moval": "function",
	"movao": "function",
	"movaq": "function",
	"movaw": "function",
	"movb": "function",
	"movc3": "function",
	"movc5": "function",
	"movd": "function",
	"movf": "function",
	"movg": "function",
	"movh": "function",
	"movl": "function",
	"movo": "function",
	"movp": "function",
	"movpsl": "function",
	"movq": "function",
	"movtc": "function",
	"movtuc": "function",
	"movw": "function",
	"movzbl": "function",
	"movzbw": "function",
	"movzwl": "function",
	"mtpr": "function",
	"mtvp": "function",
	"mulb2": "function",
	"mulb3": "function",
	"muld2": "function",
	"muld3": "function",
	"mulf2": "function",
	"mulf3": "function",
	"mulg2": "function",
	"mulg3": "function",
	"mulh2": "function",
	"mulh3": "function",
	"mull2": "function",
	"mull3": "function",
	"mulp": "function",
	"mulw2": "function",
	"mulw3": "function",
	"nop": "function",
	"pc": "keyword3",
	"polyd": "function",
	"polyf": "function",
	"polyg": "function",
	"polyh": "function",
	"popr": "function",
	"prober": "function",
	"probew": "function",
	"pushab": "function",
	"pushabl": "function",
	"pushad": "function",
	"pushaf": "function",
	"pushag": "function",
	"pushah": "function",
	"pushal": "function",
	"pushao": "function",
	"pushaq": "function",
	"pushaw": "function",
	"pushl": "function",
	"pushr": "function",
	"r0": "keyword3",
	"r1": "keyword3",
	"r10": "keyword3",
	"r11": "keyword3",
	"r12": "keyword3",
	"r2": "keyword3",
	"r3": "keyword3",
	"r4": "keyword3",
	"r5": "keyword3",
	"r6": "keyword3",
	"r7": "keyword3",
	"r8": "keyword3",
	"r9": "keyword3",
	"rei": "function",
	"remqhi": "function",
	"remqti": "function",
	"remque": "function",
	"ret": "function",
	"rotl": "function",
	"rsb": "function",
	"sbwc": "function",
	"scanc": "function",
	"skpc": "function",
	"sobgeq": "function",
	"sobgtr": "function",
	"sp": "keyword3",
	"spanc": "function",
	"subb2": "function",
	"subb3": "function",
	"subd2": "function",
	"subd3": "function",
	"subf2": "function",
	"subf3": "function",
	"subg2": "function",
	"subg3": "function",
	"subh2": "function",
	"subh3": "function",
	"subl2": "function",
	"subl3": "function",
	"subp4": "function",
	"subp6": "function",
	"subw2": "function",
	"subw3": "function",
	"svpctx": "function",
	"tstb": "function",
	"tstd": "function",
	"tstf": "function",
	"tstg": "function",
	"tsth": "function",
	"tstl": "function",
	"tstw": "function",
	"vgathl": "function",
	"vgathq": "function",
	"vldl": "function",
	"vldq": "function",
	"vsaddd": "function",
	"vsaddf": "function",
	"vsaddg": "function",
	"vsaddl": "function",
	"vsbicl": "function",
	"vsbisl": "function",
	"vscatl": "function",
	"vscatq": "function",
	"vscmpd": "function",
	"vscmpf": "function",
	"vscmpg": "function",
	"vscmpl": "function",
	"vsdivd": "function",
	"vsdivf": "function",
	"vsdivg": "function",
	"vsmerge": "function",
	"vsmuld": "function",
	"vsmulf": "function",
	"vsmulg": "function",
	"vsmull": "function",
	"vsslll": "function",
	"vssrll": "function",
	"vssubd": "function",
	"vssubf": "function",
	"vssubg": "function",
	"vssubl": "function",
	"vstl": "function",
	"vstq": "function",
	"vsxorl": "function",
	"vsync": "function",
	"vvaddd": "function",
	"vvaddf": "function",
	"vvaddg": "function",
	"vvaddl": "function",
	"vvbicl": "function",
	"vvbisl": "function",
	"vvcmpd": "function",
	"vvcmpf": "function",
	"vvcmpg": "function",
	"vvcmpl": "function",
	"vvcvt": "function",
	"vvdivd": "function",
	"vvdivf": "function",
	"vvdivg": "function",
	"vvmerge": "function",
	"vvmuld": "function",
	"vvmulf": "function",
	"vvmulg": "function",
	"vvmull": "function",
	"vvslll": "function",
	"vvsrll": "function",
	"vvsubd": "function",
	"vvsubf": "function",
	"vvsubg": "function",
	"vvsubl": "function",
	"vvxorl": "function",
	"xfc": "function",
	"xorb2": "function",
	"xorb3": "function",
	"xorl2": "function",
	"xorl3": "function",
	"xorw2": "function",
	"xorw3": "function",
}

# Dictionary of keywords dictionaries for assembly_macro32 mode.
keywordsDictDict = {
	"assembly_macro32_main": assembly_macro32_main_keywords_dict,
}

# Rules for assembly_macro32_main ruleset.

def assembly_macro32_rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def assembly_macro32_rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def assembly_macro32_rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def assembly_macro32_rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern="%%",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def assembly_macro32_rule4(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="%",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def assembly_macro32_rule5(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def assembly_macro32_rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="B^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="D^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="O^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="X^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="A^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="M^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="F^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="C^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="L^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="G^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_macro32_rule26(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for assembly_macro32_main ruleset.
rulesDict1 = {
	"!": [assembly_macro32_rule24,],
	"\"": [assembly_macro32_rule2,],
	"#": [assembly_macro32_rule22,],
	"%": [assembly_macro32_rule3,assembly_macro32_rule4,],
	"&": [assembly_macro32_rule23,],
	"'": [assembly_macro32_rule1,],
	"*": [assembly_macro32_rule20,],
	"+": [assembly_macro32_rule17,],
	"-": [assembly_macro32_rule18,],
	".": [assembly_macro32_rule26,],
	"/": [assembly_macro32_rule19,],
	"0": [assembly_macro32_rule26,],
	"1": [assembly_macro32_rule26,],
	"2": [assembly_macro32_rule26,],
	"3": [assembly_macro32_rule26,],
	"4": [assembly_macro32_rule26,],
	"5": [assembly_macro32_rule26,],
	"6": [assembly_macro32_rule26,],
	"7": [assembly_macro32_rule26,],
	"8": [assembly_macro32_rule26,],
	"9": [assembly_macro32_rule26,],
	":": [assembly_macro32_rule5,],
	";": [assembly_macro32_rule0,],
	"@": [assembly_macro32_rule21,assembly_macro32_rule26,],
	"A": [assembly_macro32_rule10,assembly_macro32_rule26,],
	"B": [assembly_macro32_rule6,assembly_macro32_rule26,],
	"C": [assembly_macro32_rule13,assembly_macro32_rule26,],
	"D": [assembly_macro32_rule7,assembly_macro32_rule26,],
	"E": [assembly_macro32_rule26,],
	"F": [assembly_macro32_rule12,assembly_macro32_rule26,],
	"G": [assembly_macro32_rule15,assembly_macro32_rule26,],
	"H": [assembly_macro32_rule26,],
	"I": [assembly_macro32_rule26,],
	"J": [assembly_macro32_rule26,],
	"K": [assembly_macro32_rule26,],
	"L": [assembly_macro32_rule14,assembly_macro32_rule26,],
	"M": [assembly_macro32_rule11,assembly_macro32_rule26,],
	"N": [assembly_macro32_rule26,],
	"O": [assembly_macro32_rule8,assembly_macro32_rule26,],
	"P": [assembly_macro32_rule26,],
	"Q": [assembly_macro32_rule26,],
	"R": [assembly_macro32_rule26,],
	"S": [assembly_macro32_rule26,],
	"T": [assembly_macro32_rule26,],
	"U": [assembly_macro32_rule26,],
	"V": [assembly_macro32_rule26,],
	"W": [assembly_macro32_rule26,],
	"X": [assembly_macro32_rule9,assembly_macro32_rule26,],
	"Y": [assembly_macro32_rule26,],
	"Z": [assembly_macro32_rule26,],
	"\\": [assembly_macro32_rule25,],
	"^": [assembly_macro32_rule16,],
	"_": [assembly_macro32_rule26,],
	"a": [assembly_macro32_rule26,],
	"b": [assembly_macro32_rule26,],
	"c": [assembly_macro32_rule26,],
	"d": [assembly_macro32_rule26,],
	"e": [assembly_macro32_rule26,],
	"f": [assembly_macro32_rule26,],
	"g": [assembly_macro32_rule26,],
	"h": [assembly_macro32_rule26,],
	"i": [assembly_macro32_rule26,],
	"j": [assembly_macro32_rule26,],
	"k": [assembly_macro32_rule26,],
	"l": [assembly_macro32_rule26,],
	"m": [assembly_macro32_rule26,],
	"n": [assembly_macro32_rule26,],
	"o": [assembly_macro32_rule26,],
	"p": [assembly_macro32_rule26,],
	"q": [assembly_macro32_rule26,],
	"r": [assembly_macro32_rule26,],
	"s": [assembly_macro32_rule26,],
	"t": [assembly_macro32_rule26,],
	"u": [assembly_macro32_rule26,],
	"v": [assembly_macro32_rule26,],
	"w": [assembly_macro32_rule26,],
	"x": [assembly_macro32_rule26,],
	"y": [assembly_macro32_rule26,],
	"z": [assembly_macro32_rule26,],
}

# x.rulesDictDict for assembly_macro32 mode.
rulesDictDict = {
	"assembly_macro32_main": rulesDict1,
}

# Import dict for assembly_macro32 mode.
importDict = {}

