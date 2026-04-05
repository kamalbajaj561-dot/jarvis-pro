from jarvis.main import JarvisPro


def test_open_project_guidance_when_missing_path():
    j = JarvisPro(voice_mode=False)
    result = j.handle_command("open my project")
    assert not result.ok


def test_run_project_guidance_when_missing_path():
    j = JarvisPro(voice_mode=False)
    result = j.handle_command("run my project")
    assert not result.ok


def test_fix_error_guidance():
    j = JarvisPro(voice_mode=False)
    result = j.handle_command("fix my app error")
    assert result.ok


def test_whatsapp_intent():
    j = JarvisPro(voice_mode=False)
    result = j.handle_command("tell Rahul I will call later")
    assert result.ok


def test_web_search_intent():
    j = JarvisPro(voice_mode=False)
    result = j.handle_command("search python unit test mocking")
    assert result.ok


def test_business_intent():
    j = JarvisPro(voice_mode=False)
    result = j.handle_command("startup revenue strategy")
    assert result.ok


def test_risky_action_requires_confirmation():
    j = JarvisPro(voice_mode=False)
    result = j.handle_command("shutdown now")
    assert not result.ok
    assert "risky" in result.message.lower()


def test_generic_chat():
    j = JarvisPro(voice_mode=False)
    result = j.handle_command("hello there")
    assert result.ok
