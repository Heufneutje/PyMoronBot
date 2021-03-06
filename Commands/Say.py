# -*- coding: utf-8 -*-
"""
Created on Dec 20, 2011

@author: Tyranic-Moron
"""

from IRCMessage import IRCMessage
from IRCResponse import IRCResponse, ResponseType
from CommandInterface import CommandInterface


class Say(CommandInterface):
    triggers = ['say']
    help = 'say [channel] <text> - makes the bot repeat the specified text'

    def execute(self, message):
        """
        @type message: IRCMessage
        """
        if not message.ParameterList:
            return IRCResponse(ResponseType.Say, 'Say what?', message.ReplyTo)
        
        if message.ParameterList[0] in self.bot.channels:
            return IRCResponse(ResponseType.Say, u" ".join(message.ParameterList[1:]), message.ParameterList[0])
        
        return IRCResponse(ResponseType.Say, message.Parameters, message.ReplyTo)
