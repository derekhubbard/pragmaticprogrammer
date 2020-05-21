from pathlib import Path
import json
import yaml

def main(d: Path):
    assert d.exists()
    assert d.is_dir()

    for yaml_file in d.glob("*.yml"):
        with yaml_file.open() as f:
            data = yaml.safe_load(f)

        json_file = d / f"{yaml_file.stem}.json"

        with json_file.open(mode="w") as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    directory = Path("./files")
    main(directory)