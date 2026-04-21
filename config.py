# encoding: utf-8
import os

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = 'makai-dog'
TOKEN = os.getenv("GITHUB_TOKEN")

# The repository to add this issue to
REPO_OWNER = 'makai-dog'
REPO_NAME = 'KAI_ChatDailyPapers'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/cs/new'

# Keywords to search
KEYWORD_LIST = ["Robotics", "AI", "Machine Learning", "Computer Vision", "Natural Language Processing", "Robotics", "AI", "Machine Learning", "Computer Vision", "Natural Language Processing", "MPC", "VLA"]


OPENAI_API_KEYS = [os.getenv("OPENAI_API_KEY"),]

LANGUAGE = "zh"  # zh | en
