# tests/test_smoke.py
import subprocess, sys
def test_script_runs_and_prints_emoji():
    result = subprocess.run(
        [sys.executable, "make_emoji.py", "--name", ":sparkles:", "--msg", "Hello"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "✨" in result.stdout # sparkles emoji