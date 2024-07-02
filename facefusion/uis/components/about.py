from typing import Optional
import gradio

from facefusion import metadata, wording

ABOUT_BUTTON : Optional[gradio.HTML] = None
DONATE_BUTTON : Optional[gradio.HTML] = None


def render() -> None:
	global ABOUT_BUTTON
	global DONATE_BUTTON

	ABOUT_BUTTON = gradio.HTML(
		value='<img src="file/bLogo.png" />'
	)
	DONATE_BUTTON = gradio.Button(
		value = '"استكشف قوة الذكاء الاصطناعي في تركيب وتبديل الوجوه! اشترك الآن في القناة لاكتشاف مجموعة فيديوهات مذهلة تعرض كيفية تطبيق هذه التقنيات في الواقع. لن تندم، اشترك اليوم واكتشف ما يمكن أن يفعله الذكاء الاصطناعي!',
		link = 'https://www.youtube.com/@ahmedroshbaik/?sub_confirmation=1',
		size = 'sm'
	)
