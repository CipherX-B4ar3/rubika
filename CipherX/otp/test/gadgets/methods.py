import os
import re
import sys
import json
import time
import random
import warnings
from .classino import Classino

file = """
{
    "users": {
        "Values": ["Block", "Unblock"],
        "GetUserInfo": {
            "params": {
                "user_guid": {"types": "str"}
            }
        },
        "SetBlockUser": {
            "params": {
                "user_guid": {"types": "str"},
                "action": {"types": ["str", "optional"], "alloweds": ["Block", "Unblock"], "default": "Block"}
            }
        },
        "DeleteUserChat": {
            "params": {
                "user_guid": {"types": "str"},
                "last_deleted_message_id": {"types": ["str", "int"], "func": "to_string"}
            }
        },
        "CheckUserUsername": {
            "params": {
                "username": {"types": "str"}
            }
        }
    },
    "chats": {
        "Values": ["Mute", "Unmute", "Typing", "Uploading", "Recording", "Text", "Hashtag"],
        "UploadAvatar": {
            "params": {
                "object_guid": {"types": "str"},
                "main_file_id":  {"types": "str"},
                "thumbnail_file_id": {"types": "str"}
            }
        },
        "DeleteAvatar": {
            "params": {
                "object_guid": {"types": "str"},
                "avatar_id": {"types": "str"}
            }
        },
        "GetAvatars": {
            "params": {
                "object_guid": {"types": "str"}
            }
        },
        "GetChats": {
            "params": {
                "start_id": {"types": ["int", "str"], "func": "to_number", "default": 0}
            }
        },
        "SeenChats": {
            "params": {
                "seen_list": {"types": "dict", "func": "to_array"}
            }
        },
        "GetChatAds": {
            "params": {
                "state": {"types": ["int", "str"], "defualt": {"func": "timestamp"}, "func": "to_number"}
            }
        },
        "SetActionChat": {
            "params": {
                "object_guid": {"types": "str"},
                "action": {"types": ["str", "optional"], "alloweds": ["Mute", "Unmute"], "default": "Mute"}
            }
        },
        "GetChatsUpdates": {
            "params": {
                "state": {"types": ["int", "str"], "defualt": {"func": "timestamp"}, "func": "to_number"}
            }
        },
        "SendChatActivity": {
            "params": {
                "object_guid": {"types": "str"},
                "activity": {"types": ["str", "optional"], "alloweds": ["Typing", "Uploading", "Recording"], "default": "Typing"}
            }
        },
        "DeleteChatHistory": {
            "params": {
                "object_guid": {"types": "str"}
            }
        },
        "SearchChatMessages": {
            "params": {
                "object_guid": {"types": "str"},
                "search_text": {"types": "str"},
                "type": {"types": ["str", "optional"], "alloweds": ["Text", "Hashtag"], "default": "Hashtag"}
            }
        }

    },
    "extras": {
        "Values": [],
        "SearchGlobalObjects": {
            "params": {
                "search_text": {"types": "str"}
            }
        },
        "GetAbsObjects": {
            "params": {
                "objects_guids": {"types": ["str", "list"], "func": "to_array"}
            }
        },
        "GetObjectByUsername": {
            "params": {
                "username": {"types": "str"}
            }
        },
        "GetLinkFromAppUrl": {
            "params": {
                "app_url": {"types": "str"}
            }
        }
    },
    "groups": {
        "Values": ["Set", "Unset", "SetAdmin", "UnsetAdmin", "Hidden", "Visible", "AddMember", "ViewAdmins", "ViewMembers", "SendMessages", "SetAdmin", "BanMember", "ChangeInfo", "PinMessages", "SetJoinLink", "SetMemberAccess", "DeleteGlobalAllMessages"],
        "AddGroup": {
            "params": {
                "title": {"types": "str"},
                "member_guids": {"types": ["str", "list"], "func": "to_array"}
            }
        },
        "JoinGroup": {
            "params": {
                "link": {"types": "str", "func": "get_hash_link"}
            }
        },
        "LeaveGroup": {
            "params": {
                "group_guid": {"types": "str"}
            }
        },
        "RemoveGroup": {
            "params": {
                "group_guid": {"types": "str"}
            }
        },
        "GetGroupInfo": {
            "params": {
                "group_guid": {"types": "str"}
            }
        },
        "GetGroupLink": {
            "params": {
                "group_guid": {"types": "str"}
            }
        },
        "SetGroupLink": {
            "params": {
                "group_guid": {"types": "str"}
            }
        },
        "EditGroupInfo": {
            "updated_parameters": true,
            "params": {
                "group_guid": {"types": "str"},
                "title": {"types": ["str", "optional"]},
                "description": {"types": ["str", "optional"]},
                "chat_history_for_new_members": {"types": ["str", "optional"], "alloweds": ["Hidden", "Visible"]}
            }
        },
        "SetGroupAdmin": {
            "params": {
                "group_guid": {"types": "str"},
                "member_guid": {"types": "str"},
                "access_list": {"types": ["str", "list"], "alloweds": ["SetAdmin", "BanMember", "ChangeInfo", "PinMessages", "SetJoinLink", "SetMemberAccess", "DeleteGlobalAllMessages"], "func": "to_array"},
                "action": {"types": ["str", "optional"], "alloweds": ["SetAdmin", "UnsetAdmin"], "default": "SetAdmin"}
            }
        },
        "BanGroupMember": {
            "params": {
                "group_guid": {"types": "str"},
                "member_guid": {"types": "str"},
                "action": {"types": ["str", "optional"], "alloweds": ["Set", "Unset"], "default": "Set"}
            }
        },
        "AddGroupMembers": {
            "params": {
                "group_guid": {"types": "str"},
                "member_guids": {"types": ["str", "list"], "func": "to_array"}
            }
        },
        "GetGroupAllMembers": {
            "params": {
                "group_guid": {"types": "str"},
                "search_text": {"types": ["str", "optional"], "default": ""},
                "start_id": {"types": ["int", "str"], "func": "to_number", "default": 0}
            }
        },
        "GetGroupAdminMembers": {
            "params": {
                "group_guid": {"types": "str"},
                "start_id": {"types": ["int", "str"], "func": "to_number", "default": 0}
            }
        },
        "GetGroupMentionList": {
            "params": {
                "group_guid": {"types": "str"},
                "search_mention": {"types": ["str", "optional"], "default": ""}
            }
        },
        "GetGroupDefaultAccess": {
            "params": {
                "group_guid": {"types": "str"}

            }
        },
        "SetGroupDefaultAccess": {
            "params": {
                "group_guid": {"types": "str"},
                "access_list": {"types": ["str", "list"], "alloweds": ["AddMember", "ViewAdmins", "ViewMembers", "SendMessages"]}
            }
        },
        "GroupPreviewByJoinLink": {
            "params": {
                "link": {"types": "str", "func": "get_hash_link"}
            }
        },
        "DeleteNoAccessGroupChat": {
            "params": {
                "group_guid": {"types": "str"}
            }
        },
        "GetGroupAdminAccessList": {
            "params": {
                "group_guid": {"types": "str"},
                "member_guid": {"types": "str"}
            }
        }
    },
    "messages": {
        "Values": [
            "Pin","Unpin", "Text", "Gif", "File", "Image", "Voice", "Music", "Video", "FileInline", "Quiz", "Regular", "FromMin", "FromMax", "Local", "Global"],
        "SendMessage": {
            "params": {
                "object_guid": {"types": "str"},
                "message": {
                    "types": ["dict", "object", "str", "optional"],
                    "ifs": {
                        "str": {"func": "to_metadata", "unpack": true},
                        "otherwise": {"cname": "sticker", "func": "to_array"}
                    }
                },
                "reply_to_message_id": {
                    "types": ["str", "int", "optional"],
                    "func": "to_string"
                },
                "file_inline": {
                    "types": ["object", "dict", "optional"],
                    "func": "to_string"
                },
                "type": {"types": ["str", "optional"], "alloweds": ["FileInlineCaption", "FileInline"], "default": "FileInline"},
                "rnd": {"types": ["str", "int", "optional"], "default": {"func": "random_number"}, "func": "to_string"}
            }
        },
        "EditMessage": {
            "params": {
                "object_guid": {"types": "str"},
                "message_id": {"types": ["str", "int"], "func": "to_string"},
                "text": {"types": "str", "func": "to_metadata", "unpack": true}
            }
        },
        "DeleteMessages": {
            "params": {
                "object_guid": {"types": "str"},
                "message_ids": {"types": ["int", "str", "list"], "func": "to_array"},
                "type": {"types": ["str", "optional"], "alloweds": ["Local", "Global"], "default": "Global"}
            }
        },
        "RequestSendFile": {
            "params": {
                "filename": {"cname": "file_name", "types": "str"},
                "size": {"types": ["str", "int", "float"], "func": "to_number"},
                "mime": {"types": ["str", "optional"], "heirship": ["file_name"], "func": "get_format"}
            }
        },
        "ForwardMessages": {
            "params": {
                "from_object_guid": {"types": "str"},
                "to_object_guid": {"types": "str"},
                "message_ids": {"types": ["int", "str", "list"], "func": "to_array"},
                "rnd": {"types": ["str", "int", "optional"], "default": {"func": "random_number"}, "func": "to_string"}
            }
        },
        "CreatePoll": {
            "params": {
                "object_guid": {"types": "str"},
                "question": {"types": "str", "func": "to_metadata", "unpack": true},
                "options": {"types": "list", "minimum": 2},
                "type": {"types": ["str", "optional"], "alloweds": ["Quiz", "Regular"], "default": "Regular"},
                "is_anonymous": {"types": ["bool", "optional"], "default": true},
                "allows_multiple_answers": {"types": ["bool", "optional"], "default": false},
                "correct_option_index": {"types": ["str", "int", "optional"], "default": 0, "func": "to_number"},
                "explanation": {"types": ["str", "optional"]},
                "rnd": {"types": ["str", "int", "optional"], "default": {"func": "random_number"}, "func": "to_string"}
            }
        },
        "VotePoll": {
            "params": {
                "poll_id": {"types": "str"},
                "selection_index": {"types": ["int", "str"], "func": "to_number"}
            }
        },
        "GetPollStatus": {
            "params": {
                "poll_id": {"types": "str"}
            }
        },
        "GetPollOptionVoters": {
            "params": {
                "poll_id": {"types": "str"},
                "selection_index": {"types": ["int", "str"], "func": "to_number"},
                "start_id": {"types": ["int", "str"], "func": "to_number", "default": 0}
            }
        },
        "SetPinMessage": {
            "params": {
                "object_guid": {"types": "str"},
                "message_id": {"types": ["str", "int"], "func": "to_string"},
                "action": {"types": ["str", "optional"], "alloweds": ["Pin", "Unpin"], "default": "Pin"}
            }
        },
        "GetMessagesUpdates": {
            "params": {
                "object_guid": {"types": "str"},
                "state": {"types": ["int", "str"], "defualt": {"func": "timestamp"}, "func": "to_number"}
            }
        },
        "SearchGlobalMessages": {
            "params": {
                "search_text": {"types": "str"},
                "type": {"types": ["str", "optional"], "alloweds": ["Text"], "default": "Text"}
            }
        },
        "ClickMessageUrl": {
            "params": {
                "object_guid": {"types": "str"},
                "message_id": {"types": ["str", "int"], "func": "to_string"},
                "link_url": {"types": "str"}
            }
        },
        "GetMessagesByID": {
            "params": {
                "object_guid": {"types": "str"},
                "message_ids": {"types": ["int", "str", "list"], "func": "to_array"}
            }
        },
        "GetMessages": {
            "params": {
                "object_guid": {"types": "str"},
                "sort": {"types": ["str", "optional"], "alloweds": ["FromMin", "FromMax"], "default": "FromMin"},
                "min_id": {"types": ["str", "int"], "func": "to_number"},
                "max_id": {"types": ["str", "int"], "func": "to_number"},
                "limit": {"types": ["str", "int"], "func": "to_number", "default": 10},
                "type": {"types": ["str", "optional"]}
            }
        },
        "GetMessagesInterval": {
            "params": {
                "object_guid": {"types": "str"},
                "middle_message_id": {"types": ["str", "int"], "func": "to_string"},
                "type": {"types": ["str", "optional"]}
            }
        }
    },
    "channels": {
        "Values": ["Join", "Remove", "Archive", "Set", "Unset"],
        "AddChannel": {
            "params": {
                "title": {"types": "str"},
                "description": {"types": ["str", "optional"]}
            }
        },
        "RemoveChannel": {
            "params": {
                "channel_guid": {"types": "str"}
            }
        },
        "GetChannelInfo": {
            "params": {
                "channel_guid": {"types": "str"}
            }
        },
        "EditChannelInfo": {
            "updated_parameters": true,
            "params": {
                "channel_guid": {"types": "str"},
                "title": {"types": "str"},
                "description": {"types": ["str", "optional"]},
                "channel_type": {"types": ["str", "optional"], "alloweds": ["Public", "Private"]},
                "sign_messages": {"types": ["str", "optional"]}
            }
        },
        "JoinChannelAction": {
            "params": {
                "channel_guid": {"types": "str"},
                "action": {"types": ["str", "optional"], "alloweds": ["Join", "Remove", "Archive"], "default": "Join"}
            }
        },
        "JoinChannelByLink": {
            "params": {
                "link": {"types": "str", "cname": "hash_link", "func": "get_hash_link"}
            }
        },
        "AddChannelMembers": {
            "params": {
                "channel_guid": {"types": "str"},
                "member_guids": {"types": ["str", "list"], "func": "to_array"}
            }
        },
        "BanChannelMember": {
            "params": {
                "channel_guid": {"types": "str"},
                "member_guid": {"types": "str"},
                "action": {"types": ["str", "optional"], "alloweds": ["Set", "Unset"], "default": "Set"}
            }
        },
        "CheckChannelUsername": {
            "params": {
                "username": {"types": "str"}
            }
        },
        "ChannelPreviewByJoinLink": {
            "params": {
                "link": {"types": "str", "cname": "hash_link", "func": "get_hash_link"}
            }
        },
        "GetChannelAllMembers": {
            "params": {
                "channel_guid": {"types": "str"},
                "search_text": {"types": ["str", "optional"], "default": ""},
                "start_id": {"types": ["int", "str"], "func": "to_number", "default": 0}
            }
        },
        "GetChannelAdminMembers": {
            "params": {
                "channel_guid": {"types": "str"},
                "start_id": {"types": ["int", "str"], "func": "to_number", "default": 0}
            }
        },
        "UpdateChannelUsername": {
            "params": {
                "channel_guid": {"types": "str"},
                "username": {"types": "str"}
            }
        },
        "GetChannelLink": {
            "params": {
                "channel_guid": {"types": "str"}
            }
        },
        "SetChannelLink": {
            "params": {
                "channel_guid": {"types": "str"}
            }
        },
        "GetChannelAdminAccessList": {
            "params": {
                "channel_guid": {"types": "str"},
                "member_guid": {"types": "str"}
            }
        }
    },
    "conracts": {
        "Values": [],
        "DeleteContact": {
            "params": {
                "user_guid": {"types": "str"}
            }
        },
        "AddAddressBook": {
            "params": {
                "phone": {"types": "str", "func": "get_phone"},
                "first_name": {"types": "str"},
                "last_name": {"types": ["str", "optional"], "default": ""}
            }
        },
        "GetContactsUpdates": {
            "params": {
                "state": {"types": ["int", "str"], "defualt": {"func": "timestamp"}, "func": "to_number"}
            }
        },
        "GetContacts": {
            "params": {
                "start_id": {"types": ["int", "str"], "func": "to_number", "default": 0}
            }
        }
    },
    "settings": {
        "Values": ["Nobody", "Everybody", "MyContacts", "Bots", "Groups", "Contacts", "Channels", "NonConatcts"],
        "SetSetting": {
            "updated_parameters": true,
            "params": {
                "show_my_last_online": {"types": ["str", "optional"], "alloweds": ["Nobody", "Everybody", "MyContacts"]},
                "show_my_phone_number": {"types": ["str", "optional"], "alloweds": ["Nobody", "Everybody", "MyContacts"]},
                "show_my_profile_photo": {"types": ["str", "optional"], "alloweds": ["Everybody", "MyContacts"]},
                "link_forward_message": {"types": ["str", "optional"], "alloweds": ["Nobody", "Everybody", "MyContacts"]},
                "can_join_chat_by": {"types": ["str", "optional"], "alloweds": ["Everybody", "MyContacts"]}
            }
        },
        "AddFolder": {
            "params": {
                "cname": {"types": "str"},
                "include_chat_types": {
                    "types": ["str", "list", "optional"],
                    "alloweds": ["Bots", "Groups", "Contacts", "Channels", "NonConatcts"], "func": "to_array", "default": []},
                "exclude_chat_types": {
                    "types": ["str", "list", "optional"],
                    "alloweds": ["Bots", "Groups", "Contacts", "Channels", "NonConatcts"], "func": "to_array", "default": []},
                "include_object_guids": {"types": ["str", "list", "optional"], "func": "to_array", "default": []},
                "exclude_object_guids": {"types": ["str", "list", "optional"], "func": "to_array", "default": []}
            }
        },
        "GetFolders": {
            "params": {
                "last_state": {"types": ["int", "str"], "defualt": {"func": "timestamp"}, "func": "to_number"}
            }
        },
        "EditFolder": {
            "updated_parameters": true,
            "params": {
                "cname": {"types": "str"},
                "include_chat_types": {
                    "types": ["str", "list", "optional"],
                    "alloweds": ["Bots", "Groups", "Contacts", "Channels", "NonConatcts"], "func": "to_array", "default": []},
                "exclude_chat_types": {
                    "types": ["str", "list", "optional"],
                    "alloweds": ["Bots", "Groups", "Contacts", "Channels", "NonConatcts"], "func": "to_array", "default": []},
                "include_object_guids": {"types": ["str", "list", "optional"], "func": "to_array", "default": []},
                "exclude_object_guids": {"types": ["str", "list", "optional"], "func": "to_array", "default": []}
            }
        },
        "DeleteFolder": {
            "params": {
                "folder_id": {"types": "str"}
            }
        },
        "UpdateProfile": {
            "updated_parameters": true,
            "params": {
                "first_name": {"types": ["str", "optional"]},
                "last_name": {"types": ["str", "optional"]},
                "bio": {"types": ["str", "optional"]}
            }
        },
        "UpdateUsername": {
            "params": {
                "username": {"types": "str"}
            }
        },
        "GetTwoPasscodeStatus": null,
        "GetSuggestedFolders": null,
        "GetPrivacySetting": null,
        "GetBlockedUsers": null,
        "GetMySessions": null,
        "TerminateSession": {
            "params": {
                "session_key": {"types": "str"}
            }
        },
        "SetupTwoStepVerification": {
            "params": {
                "password": {"types": ["str", "int"], "func": "to_string"},
                "hint": {"types": ["str", "int"], "func": "to_string"},
                "recovery_email": {"types": "str"}
            }
        }
    },
    "stickers": {
        "Values": ["All", "Add", "Remove"],
        "GetMyStickerSets": null,
        "SearchStickers": {
            "params": {
                "search_text": {"types": ["str", "optional"], "default": ""},
                "start_id": {"types": ["int", "str"], "func": "to_number", "default": 0}
            }
        },
        "GetStickerSetByID": {
            "params": {
                "sticker_set_id": {"types": "str"}
            }
        },
        "ActionOnStickerSet": {
            "params": {
                "sticker_set_id": {"types": "str"},
                "action": {"types": ["str", "optional"], "alloweds": ["Add", "Remove"], "default": "Add"}
            }
        },
        "GetStickersByEmoji": {
            "params": {
                "emoji": {"types": "str", "cname": "emoji_character"},
                "suggest_by": {"types": ["str", "optional"], "default": "Add"}
            }
        },
        "GetStickersBySetIDs": {
            "params": {
                "sticker_set_ids": {"types": ["str", "list"], "func": "to_array"}
            }
        },
        "GetTrendStickerSets": {
            "params": {
                "start_id": {"types": ["int", "str"], "func": "to_number", "default": 0}
            }
        }

    },
    "authorisations": {
        "Values": ["SMS", "Internal"],
        "GetDCs": {
            "urls": ["https://getdcmess.iranlms.ir/"],
            "encrypt": false,
            "params": {
                "api_version": {"types": ["int", "str"], "func": "to_string", "default": "4"}
            }
        },
        "SignIn": {
            "tmp_session": true,
            "params": {
                "phone_code": {"types": "str"},
                "phone_number": {"types": "str", "func": "get_phone"},
                "phone_code_hash": {"types": "str"}
            }
        },
        "SendCode": {
            "tmp_session": true,
            "params": {
                "phone_number": {"types": "str", "func": "get_phone"},
                "pass_key": {"types": ["str", "optional"], "default": null},
                "send_type": {"types": ["str", "optional"], "alloweds": ["SMS", "Internal"], "default": "SMS"}
            }
        },
        "RegisterDevice": {
            "params": {
                "uaer_agent": {"types": "str", "func": "get_browser", "unpack": true},
                "app_version": {"types": "str"},
                "lang_code": {"types": ["str", "optional"], "default": "fa"}
            }
        },
        "LoginDisableTwoStep": {
            "tmp_session": true,
            "params": {
                "phone_number": {"types": "str", "func": "get_phone"},
                "email_code": {"types": ["str", "int"], "func": "to_string"},
                "forget_password_code_hash": {"types": "str"}
            }
        }
    }
}
"""
grouping = json.loads(file)


class Functions:
    system_versions = {
        'Windows NT 10.0': 'Windows 10',
        'Windows NT 6.2': 'Windows 8',
        'Windows NT 6.1': 'Windows 7',
        'Windows NT 6.0': 'Windows Vista',
        'Windows NT 5.1': 'windows XP',
        'Windows NT 5.0': 'Windows 2000',
        'Mac': 'Mac/iOS',
        'X11': 'UNIX',
        'Linux': 'Linux'
    }

    @classmethod
    def get_phone(cls, value, *args, **kwargs):
        phone_number = ''.join(re.findall(r'\d+', value))
        if not phone_number.startswith('98'):
            phone_number = '98' + phone_number
        return phone_number

    @classmethod
    def get_browser(cls, user_agent, lang_code, app_version, *args, **kwargs):
        device_model = re.search(r'(opera|chrome|safari|firefox|msie'
                                 r'|trident)\/(\d+)', user_agent.lower())
        if not device_model:
            device_model = 'Unknown'
            warnings.warn(f'can not parse user-agent ({user_agent})')

        else:
            device_model = device_model.group(1) + ' ' + device_model.group(2)

        system_version = 'Unknown'
        for key, value in cls.system_versions.items():
            if key in user_agent:
                system_version = value
                break

        # window.navigator.mimeTypes.length (outdated . Defaults to '2')
        device_hash = '2'
        return {
            'token': '',
            'lang_code': lang_code,
            'token_type': 'Web',
            'app_version': f'WB_{app_version}',
            'system_version': system_version,
            'device_model': device_model.title(),
            'device_hash': device_hash + ''.join(re.findall(r'\d+', user_agent))}

    @classmethod
    def random_number(cls, *args, **kwargs):
        return int(random.random() * 1e6 + 1)

    @classmethod
    def timestamp(cls, *args, **kwargs):
        return int(time.time())

    @classmethod
    def get_format(cls, value, *args, **kwargs):
        return value.split('.')[-1]

    @classmethod
    def get_hash_link(cls, value, *args, **kwargs):
        return value.split('/')[-1]

    @classmethod
    def to_float(cls, value, *args, **kwargs):
        return float(value)

    @classmethod
    def to_number(cls, value, *args, **kwargs):
        return int(value)

    @classmethod
    def to_string(cls, value, *args, **kwargs):
        return str(value)

    @classmethod
    def to_array(cls, value, *args, **kwargs):
        if isinstance(value, list):
            return value

        elif isinstance(value, str):
            return [value]

        try:
            return value.to_dict()

        except AttributeError:
            try:
                return dict(value)

            except Exception:
                return value

    @classmethod
    def to_metadata(cls, value, *args, **kwargs):
        pattern = r'`(.*)`|\*\*(.*)\*\*|__(.*)__|\[(.*)\]\((\S+)\)'
        conflict = 0
        meta_data_parts = []
        for markdown in re.finditer(pattern, value):
            span = markdown.span()
            if markdown.group(0).startswith('`'):
                value = re.sub(pattern, r'\1', value, count=1)
                meta_data_parts.append(
                    {
                        'type': 'Mono',
                        'from_index': span[0] - conflict,
                        'length': span[1] - span[0] - 2
                    }
                )
                conflict += 2

            elif markdown.group(0).startswith('**'):
                value = re.sub(pattern, r'\2', value, count=1)
                meta_data_parts.append(
                    {
                        'type': 'Bold',
                        'from_index': span[0] - conflict,
                        'length': span[1] - span[0] - 4
                    }
                )
                conflict += 4

            elif markdown.group(0).startswith('__'):
                value = re.sub(pattern, r'\3', value, count=1)
                meta_data_parts.append(
                    {
                        'type': 'Italic',
                        'from_index': span[0] - conflict,
                        'length': span[1] - span[0] - 4
                    }
                )
                conflict += 4

            else:
                value = re.sub(pattern, r'\4', value, count=1)

                mention_text_object_type = 'User'
                mention_text_object_guid = markdown.group(5)
                if mention_text_object_guid.startswith('g'):
                    mention_text_object_type = 'Group'

                elif mention_text_object_guid.startswith('c'):
                    mention_text_object_type = 'Channel'

                meta_data_parts.append(
                    {
                        'type': 'MentionText',
                        'from_index': span[0] - conflict,
                        'length': len(markdown.group(4)),
                        'mention_text_object_guid': mention_text_object_guid,
                        'mention_text_object_type': mention_text_object_type
                    }
                )
                conflict += 4 + len(mention_text_object_guid)

        result = {'text': value}
        if meta_data_parts:
            result['metadata'] = {
                'meta_data_parts': meta_data_parts
            }

        return result


class BaseMethod:
    __name__ = 'CustomMethod'

    def __init__(self, method: dict, *args, **kwargs):
        self.method = method

    def __str__(self):
        result = f'{self.method_name}(*, *args, **kwargs)'

        if self.method_param:
            result += '\nArgs:\n'
            for name, param in self.method_param.items():
                types = param.get('types')
                default = param.get('default')
                alloweds = param.get('alloweds')
                heirship = param.get('heirship')

                if not isinstance(types, list):
                    types = [types]

                types = ', '.join(types)
                result += f'\t{name} ({types})\n'
                if alloweds is not None:
                    result += '\t\tthe allowed values are: '
                    result += str([alloweds])

                if default is not None:
                    result += f'\n\t\tthe default value is {default}'

                if heirship is not None:
                    result += ('\n\t\tif it is not set, it takes the'
                               f' value from the ({[alloweds]}) argument\'s')
                result += '\n'
        return result

    @property
    def method_name(self):
        return self.__name__[0].lower() + self.__name__[1:]

    @property
    def method_param(self):
        if self.method:
            if isinstance(self.method['params'], dict):
                return self.method['params']

    def build(self, argument, param, *args, **kwargs):
        ifs = param.get('ifs')
        func = param.get('func')
        types = param.get('types')
        alloweds = param.get('alloweds')

        # set defualt value
        try:
            value = self.request[argument]

        except KeyError:
            value = param['default']
            if isinstance(value, dict):
                default_func = value.get('func')
                if isinstance(default_func, str):
                    value = getattr(Functions, default_func)(
                        **value, **self.request)

        # get value heirship
        for heirship in param.get('heirship', []):
            try:
                value = self.request[heirship]
            except KeyError:
                pass

        # clall func method
        if isinstance(func, str) and value is not None:
            value = getattr(Functions, func)(value, **self.request)
            argument = param.get('cname', argument)

        # check value types
        if types and not type(value).__name__ in types:
            if value is not None and 'optional' in types:
                raise TypeError(
                    f'The given {argument} must be'
                    f' {types} not {type(value).__name__}')

        if alloweds is not None:
            if isinstance(value, list):
                for _value in value:
                    if _value not in alloweds:
                        raise ValueError(
                            f'the {argument}({_value}) value is'
                            f' not in the allowed list {alloweds}')

            elif value not in alloweds:
                raise ValueError(
                    f'the {argument}({value}) value is'
                    f' not in the allowed list {alloweds}')

        # get ifs
        if isinstance(ifs, dict):

            # move to the last key
            if 'otherwise' in ifs:
                ifs['otherwise'] = ifs.pop('otherwise')

            for operator, work in ifs.items():
                if type(value).__name__ == operator or operator == 'otherwise':
                    func = work.get('func')
                    param = work
                    if isinstance(func, str):
                        value = getattr(Functions, func)(value, **self.request)
                    break

        # to avoid adding an extra value if there is "cname"
        if argument in self.request:
            self.request.pop(argument)

        if value is not None:
            if param.get('unpack'):
                self.request.update(value)

            else:
                self.request[param.get('cname', argument)] = value

    def __call__(self, *args, **kwargs):
        if self.method_param:
            self.request = {}
            params = list(self.method['params'].keys())
            for index, value in enumerate(args):
                try:
                    self.request[params[index]] = value

                except IndexError:
                    pass

            for argument, value in kwargs.items():
                if self.method['params'].get(argument):
                    self.request[argument] = value

            for argument, param in self.method['params'].items():
                try:
                    self.build(argument, param)
                except KeyError:
                    if 'optional' not in param['types']:
                        raise TypeError(
                            f'{self.__name__}() '
                            f'required argument ({argument})')

            if self.method.get('urls') is not None:
                self.request['method'] = self.method_name

            else:
                self.request = {
                    'method': self.method_name, 'input': self.request}

            self.request['urls'] = self.method.get('urls')
            self.request['encrypt'] = self.method.get('encrypt', True)
            self.request['tmp_session'] = bool(self.method.get('tmp_session'))

            return self.request
        else:
            return {
                'urls': None,
                'input': {},
                'method': self.method_name,
                'encrypt': True,
                'tmp_session': False}


class BaseGrouping(Classino):
    def __init__(self, methods: dict, *args, **kwargs):
        self.methods = methods

    def __dir__(self):
        methods = list(self.methods.keys())
        methods.remove('Values')
        return self.methods['Values'] + methods

    def __getattr__(self, name) -> BaseMethod:
        if name in self.methods['Values']:
            return name

        method = self.create(name, (BaseMethod,), dir(self))
        return method(self.methods[method.__name__])


class Methods(Classino):
    def __init__(self, name, *args, **kwargs):
        self.__name__ = name

    def __dir__(self):
        return grouping.keys()

    def __getattr__(self, name) -> BaseGrouping:
        group = self.create(name, (BaseGrouping,), dir(self))
        return group(methods=grouping[group.__name__])

sys.modules[__name__] = Methods(__name__)
