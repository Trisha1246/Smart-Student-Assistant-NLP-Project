import os
import sys
import pprint
from pathlib import Path

# Import parts
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_part1 import PART1_DATA
from build_part2 import PART2_DATA
from build_part3 import PART3_DATA

# Combine
ALL_QUIZ_DATA = {}
ALL_QUIZ_DATA.update(PART1_DATA)
ALL_QUIZ_DATA.update(PART2_DATA)
ALL_QUIZ_DATA.update(PART3_DATA)

subjects = list(ALL_QUIZ_DATA.keys())
print(f"Total subjects assembled: {len(subjects)}")

# Generate app/quiz_data.py
output_path = Path(r"C:\Users\Kolla\.gemini\antigravity\brain\26db8f57-3667-4481-860a-201d7d8e8439\scratch\quiz_data.py")
output_path.parent.mkdir(parents=True, exist_ok=True)

header = '''# ==============================================================================
# Comprehensive Engineering Quiz Bank for Smart Student Assistant
# Structured by Subject -> Topic -> Questions (with Explanations & Difficulties)
# Total Subjects: 28 | Comprehensive coverage across CS, IT, and Engineering
# ==============================================================================

import random

ENGINEERING_SUBJECTS = ''' + pprint.pformat(subjects, width=100) + '''

QUIZ_DATA = ''' + pprint.pformat(ALL_QUIZ_DATA, width=120, sort_dicts=False) + '''


def get_available_subjects():
    """Return all available engineering subjects."""
    return list(QUIZ_DATA.keys())


def get_topics_for_subject(subject):
    """
    Return all sub-topics for the given subject.
    Case-insensitive matching with fallback.
    """
    if not subject:
        return ["General"]

    sub_clean = str(subject).strip().lower()
    for s_name, topic_dict in QUIZ_DATA.items():
        if s_name.lower() == sub_clean:
            return list(topic_dict.keys())

    # Partial match fallback
    for s_name, topic_dict in QUIZ_DATA.items():
        if sub_clean in s_name.lower():
            return list(topic_dict.keys())

    return ["General"]


def get_questions_for_quiz(subject, topic=None, count=10, difficulty=None):
    """
    Selects exactly `count` questions for the given subject, topic, and difficulty.
    Guarantees returning the requested number of questions (e.g. 5, 10, 15)
    by intelligently backfilling from related topics within the subject if a single
    topic has fewer questions than requested.

    Priority:
    1. Questions in the chosen topic matching the chosen difficulty.
    2. Remaining questions in the chosen topic (other difficulties).
    3. Questions in other topics of the same subject matching the chosen difficulty.
    4. Remaining questions in other topics of the same subject.
    """
    # 1. Normalize count
    try:
        count = int(count)
        if count <= 0:
            count = 10
    except (ValueError, TypeError):
        count = 10

    # 2. Case-insensitive subject lookup
    sub_clean = str(subject).strip().lower() if subject else "python"
    matched_subject = None
    for s_name in QUIZ_DATA.keys():
        if s_name.lower() == sub_clean:
            matched_subject = s_name
            break

    if not matched_subject:
        # Partial match
        for s_name in QUIZ_DATA.keys():
            if sub_clean in s_name.lower():
                matched_subject = s_name
                break

    if not matched_subject:
        matched_subject = "Python"

    topic_dict = QUIZ_DATA[matched_subject]

    # 3. Clean topic and difficulty
    chosen_topic = None
    if topic:
        t_str = str(topic).strip()
        if t_str.lower() not in ("all", "all topics", "comprehensive", ""):
            # Check if t_str matches any topic in topic_dict
            for t_name in topic_dict.keys():
                if t_name.lower() == t_str.lower():
                    chosen_topic = t_name
                    break
            if not chosen_topic:
                for t_name in topic_dict.keys():
                    if t_str.lower() in t_name.lower():
                        chosen_topic = t_name
                        break

    chosen_diff = None
    if difficulty:
        d_str = str(difficulty).strip().lower()
        if d_str in ("beginner", "intermediate", "advanced"):
            chosen_diff = d_str

    # 4. Partition pools
    # Pool A: Questions from the selected topic (if specific topic chosen)
    # Pool B: Questions from other topics of the subject
    topic_questions = []
    other_questions = []

    if chosen_topic and chosen_topic in topic_dict:
        topic_questions = list(topic_dict[chosen_topic])
        for t_name, q_list in topic_dict.items():
            if t_name != chosen_topic:
                other_questions.extend(q_list)
    else:
        # If 'all' or comprehensive, all questions are in topic_questions
        for q_list in topic_dict.values():
            topic_questions.extend(q_list)

    # 5. Build prioritized candidate tiers
    def filter_diff(q_list, target_diff):
        if not target_diff:
            return list(q_list), []
        matching = [q for q in q_list if q.get("difficulty") == target_diff]
        non_matching = [q for q in q_list if q.get("difficulty") != target_diff]
        return matching, non_matching

    # Tier 1: Topic questions matching difficulty
    # Tier 2: Topic questions with other difficulties
    tier1, tier2 = filter_diff(topic_questions, chosen_diff)
    random.shuffle(tier1)
    random.shuffle(tier2)

    # Tier 3: Other topics questions matching difficulty
    # Tier 4: Other topics questions with other difficulties
    tier3, tier4 = filter_diff(other_questions, chosen_diff)
    random.shuffle(tier3)
    random.shuffle(tier4)

    # Combine with strict uniqueness
    selected = []
    seen_questions = set()

    def add_from_tier(tier):
        for q in tier:
            q_text = q.get("question", "").strip()
            if q_text and q_text not in seen_questions:
                seen_questions.add(q_text)
                selected.append(q)
                if len(selected) >= count:
                    return True
        return False

    # Fill up to `count`
    done = add_from_tier(tier1)
    if not done:
        done = add_from_tier(tier2)
    if not done:
        done = add_from_tier(tier3)
    if not done:
        done = add_from_tier(tier4)

    # Fallback padding if count > subject capacity (e.g. requesting 20 when subject has 16)
    if len(selected) < count:
        # Borrow high quality questions from Python or Data Structures fundamentals
        fallback_subjects = ["Python", "Data Structures", "Operating Systems", "Computer Networks"]
        for fb_sub in fallback_subjects:
            if fb_sub != matched_subject and fb_sub in QUIZ_DATA:
                fb_pool = []
                for q_list in QUIZ_DATA[fb_sub].values():
                    fb_pool.extend(q_list)
                random.shuffle(fb_pool)
                for q in fb_pool:
                    q_text = q.get("question", "").strip()
                    if q_text and q_text not in seen_questions:
                        seen_questions.add(q_text)
                        selected.append(q)
                        if len(selected) >= count:
                            break
            if len(selected) >= count:
                break

    # Shuffle the final selected questions so the quiz order is dynamic and engaging
    random.shuffle(selected)
    return selected[:count]
'''

with open(output_path, "w", encoding="utf-8") as f:
    f.write(header)

print(f"Successfully generated {output_path} with size: {os.path.getsize(output_path)} bytes")
