# Project: Akrios
# Filename: commands/quote.py
#
# Capability: player
#
# Command Description: Allows the player to send a quote game wide
#
# By Jubelo

from commands import *

name = "quote"
version = 1

requirements = {'capability': ['player', 'mobile'],
                'generic_fail': "See {WHelp quote{x for help with this command.",
                'truth_checks':  ['args_required'],
                'false_checks': [],
                'target': 'target_all_player_game_post'}


@Command(**requirements)
async def quote(caller, args, **kwargs):
    buffer = outbuffer.OutBuffer(caller)

    if caller.is_player and caller.oocflags_stored['quote'] == 'false':
        buffer.add("You have the Quote channel disabled. Use the {Wtoggle{x command to enable it.")
        await buffer.write()
        return

    target_list = kwargs['target']
    args_ = kwargs['post']

    for person in target_list:
        if person.oocflags_stored['quote'] == 'false':
            continue
        if person == caller:
            name_ = "You"
            plural = ''
        else:
            name_ = '\n\r' + caller.disp_name
            plural = 's'

        buffer_target = outbuffer.OutBuffer(person)
        buffer_target.add(f"{{y{name_} Quote{plural}: '{args_[:300]}'{{x")
        await buffer_target.write()
