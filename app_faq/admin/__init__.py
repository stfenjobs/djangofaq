# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app_faq.models.answer import Answer, AnswerSuggestedEdits
from app_faq.models.bounty import (Bounty, BountyAward)
from app_faq.models.comment import Comment
from app_faq.models.favorite import Favorite
from app_faq.models.flag import Flag
from app_faq.models.help import Help
from app_faq.models.message import Message
from app_faq.models.question import Question, QuestionSuggestedEdits
from app_faq.models.tag import Tag


from app_faq.admin.answer import AnswerAdmin, AnswerSuggestedEditsAdmin
from app_faq.admin.bounty import (BountyAdmin, BountyAwardAdmin)
from app_faq.admin.comment import CommentAdmin
from app_faq.admin.favorite import FavoriteAdmin
from app_faq.admin.flag import FlagAdmin
from app_faq.admin.help import HelpAdmin
from app_faq.admin.message import MessageAdmin
from app_faq.admin.tag import TagAdmin
from app_faq.admin.question import QuestionAdmin, QuestionSuggestedEditsAdmin

admin.site.register(Answer, AnswerAdmin)
admin.site.register(AnswerSuggestedEdits, AnswerSuggestedEditsAdmin)
admin.site.register(Bounty, BountyAdmin)
admin.site.register(BountyAward, BountyAwardAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Flag, FlagAdmin)
admin.site.register(Help, HelpAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionSuggestedEdits, QuestionSuggestedEditsAdmin)
admin.site.register(Tag, TagAdmin)

"""
admin.site.register(Bounty)
admin.site.register(BountyAward)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Flag)
admin.site.register(Help)
admin.site.register(Message)
admin.site.register(Question)
admin.site.register(Tag)
"""
