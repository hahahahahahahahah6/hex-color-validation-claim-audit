import json
import tempfile
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
from hex_color_validation_claim_audit.audit import audit, claims, evidence, main
from hex_color_validation_claim_audit.phrases import HEXCOLORVALIDATION, NOHEXCOLORVALIDATION, GENERIC_NAMES

WEB = ('normalize_hex', 'hex_to_rgb', 'hex_to_rgb_percent', 'hex_to_name', 'html5_parse_simple_color')
COLOUR = ('hex2rgb', 'hex2web', 'Color')
ROUTES = [s for name in WEB for s in ('from webcolors import '+name+' as f\nf(x)', 'import webcolors as w\nw.'+name+'(x)')]
ROUTES += [s for name in COLOUR for s in ('from colour import '+name+' as f\nf(x)', 'import colour as c\nc.'+name+'(x)')]
ROUTES += ['from matplotlib.colors import is_color_like as f\nf(x)', 'import matplotlib.colors as mc\nmc.is_color_like(x)', 'import matplotlib\nmatplotlib.colors.is_color_like(x)', 'from matplotlib import colors\ncolors.is_color_like(x)']
ROUTES += ['obj.'+n+'(x)' for n in GENERIC_NAMES] + ['from lib import '+n+' as f\nf(x)' for n in GENERIC_NAMES]
NEGATIVE = ['import webcolors', 'import colour', 'import matplotlib', 'validate_hex_color(x)', 'obj.validate(x)', 'def broken(:', '"validate hex color"', 'subprocess.run(["checker"])', 'str(x)', 'repr(x)', 'pick_color(x)', 'palette(x)', 'lookup_name(x)', 'css.validate(x)', 'from lib import validate_hex_color\nwith x as validate_hex_color: pass\nvalidate_hex_color(x)', 'def validate_hex_color(x): pass\nobj.validate_hex_color(x)', 'import webcolors as w\nw = x\nw.normalize_hex(x)']
NEGATIVE += [n+'(x)' for n in WEB+COLOUR+('is_color_like',)] + ['obj.'+n+'(x)' for n in WEB+COLOUR+('is_color_like',)]
NEGATIVE += ['import webcolors as w\nw.'+n+'(x)' for n in ('rgb_to_hex','rgb_to_name','rgb_percent_to_hex','rgb_percent_to_name','name_to_hex','name_to_rgb','name_to_rgb_percent','html5_parse_legacy_color','html5_serialize_simple_color')]
NEGATIVE += ['import colour as c\nc.'+n+'(x)' for n in ('rgb2hex','web2hex','hsl2rgb','rgb2hsl')]
NEGATIVE += ['x.'+n for n in ('hex','rgb','web','hsl')]
NEGATIVE += ['import matplotlib.colors as c\nc.'+n+'(x)' for n in ('to_rgb','to_rgba','to_hex','to_rgba_array')]
NEGATIVE += ['from PIL import ImageColor\nImageColor.'+n+'(x)' for n in ('getrgb','getcolor')]
NEGATIVE += ['import validators\nvalidators.base16(x)'] + ['import re\nre.'+n+'(pattern,x)' for n in ('match','search','fullmatch')]

class AuditTests(unittest.TestCase):
    def test_phrases(self):
        for phrase in HEXCOLORVALIDATION:
            with self.subTest(phrase=phrase): self.assertTrue(claims(phrase)[0])
        for phrase in NOHEXCOLORVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase)[0], set()); self.assertTrue(claims(phrase)[1])
        self.assertEqual(claims('```\nvalidate hex color\n```'), (set(), set()))

    def test_routes(self):
        for source in ROUTES:
            with self.subTest(source=source): self.assertTrue(evidence(source))
        self.assertTrue(evidence('obj = factory()\nobj.validate_hex_color(x)'))

    def test_not_evidence(self):
        for source in NEGATIVE:
            with self.subTest(source=source): self.assertFalse(evidence(source))

    def test_findings(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); (p/'README.md').write_text('validate hex color')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'tests').mkdir(); (p/'tests/test_x.py').write_text('x.validate_hex_color(y)')
            self.assertEqual(audit(p)[0]['severity'], 'MEDIUM')
            (p/'app.py').write_text('x.validate_hex_color(y)')
            self.assertFalse(audit(p))
            (p/'README.md').write_text('no hex color validation')
            self.assertEqual(audit(p)[0]['id'], 'documented-no-hex-color-validation-claim-false')

    def test_cli(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); (p/'README.md').write_text('validate hex color')
            with redirect_stdout(StringIO()) as out: self.assertEqual(main(['audit', d, '--json']), 2)
            self.assertEqual(json.loads(out.getvalue())['findings'][0]['id'], 'documented-hex-color-validation-claim-false')
            with redirect_stdout(StringIO()): self.assertEqual(main(['audit', d, '--ignore', 'README.md']), 0)

    def test_self_audit(self):
        self.assertFalse(audit(Path(__file__).resolve().parents[1]))

if __name__ == '__main__': unittest.main()
