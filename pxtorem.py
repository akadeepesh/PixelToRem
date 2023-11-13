import re


def convert_px_to_rem(css):
    # Regular expression pattern to match pixel values
    pattern = r"(\d+)px"

    rem_css = re.sub(
        pattern, lambda match: str(round(int(match.group(1)) * 0.063, 3)) + "rem", css
    )

    return rem_css


css = """
    @import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');
@import url('https://fonts.googleapis.com/css2?family=DynaPuff&family=Noto+Serif&family=Pathway+Gothic+One&family=Sedgwick+Ave+Display&display=swap');

body{
    background-image: linear-gradient(to right, #BDC3C7 0%, #2C3E50 100%);
	etc
}

.categoryWrapper{
	height: 50px;
	width:50px;
}
"""

rem_css = convert_px_to_rem(css)
print(rem_css)
