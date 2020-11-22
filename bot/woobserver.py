"""
Not asyncronishesge webserver to store webhook data in webhooks.json

Why not async?
I'm to not smart enough yet to prevent overwrites in async :]
"""

from flask import Flask