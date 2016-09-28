# -*- coding: utf-8 -*-
import json

from schema import Schema, And, Use, Optional


fb_message = Schema(
    And(Use(json.loads), {
        "object": str,
        "entry": [
            {
                "id": str,
                "time": 1474880896215,
                "messaging": [
                    {
                        "sender": {
                            "id": str
                        },
                        "recipient": {
                            "id": str
                        },
                        "timestamp": int,
                        "message": {
                            "mid": str,
                            "seq": int,
                            "text": str
                        }
                    },
                ]
            }
        ]
    }),
    ignore_extra_keys=True
)
