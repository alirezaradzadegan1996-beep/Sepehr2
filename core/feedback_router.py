from core.response_memory import get_last_response
from core.learning_feedback import save_feedback
from core.learning_score import add_score
from core.topic_feedback import reward_topic_answer, punish_topic_answer



GOOD_WORDS = [
    "خوبه",
    "عالیه",
    "خوب بود",
    "درسته",
    "ممنون",
    "عالی"
]


BAD_WORDS = [
    "بد بود",
    "اشتباهه",
    "غلطه",
    "خوب نیست",
    "نه",
    "درست نیست"
]



def process_feedback(text):

    text = text.strip()


    last = get_last_response()


    if not last:

        return None



    feedback = None



    for word in GOOD_WORDS:

        if word in text:

            feedback = "good"
            break



    if not feedback:

        for word in BAD_WORDS:

            if word in text:

                feedback = "bad"
                break



    if not feedback:

        return None




    # ذخیره بازخورد معمولی

    save_feedback(
        last["question"],
        last["answer"],
        feedback
    )



    # امتیاز حافظه یادگیری

    add_score(
        last["question"],
        last["answer"],
        feedback
    )



    # تقویت حافظه موضوعی

    if feedback == "good":

        reward_topic_answer(
            last["answer"]
        )


    else:

        punish_topic_answer(
            last["answer"]
        )




    if feedback == "good":

        return "خوشحالم که جواب مفید بود ✅"



    return "متوجه شدم، این جواب نیاز به بهبود دارد 🧠"
