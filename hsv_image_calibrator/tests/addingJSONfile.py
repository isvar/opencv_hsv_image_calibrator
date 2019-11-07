import json
from pathlib import Path
hsv_values = {
    "lower_h": 1,
    "lower_s": 2,
    "lower_v": 1,
    "upper_h": 100,
    "upper_s": 100,
    "upper_v": 100
}

hsv_data = json.dumps(hsv_values)

Path("hsv_values.json").write_text(hsv_data)