#!/usr/bin/env python

import discord
import random
import pickle
import aiocron
import linecache
#import redis
intents = discord.Intents().all()
TOKEN = 'xxx'
client = discord.Client(intents=intents)
stars_list = ['https://imgur.com/cOOD6af', 'https://imgur.com/hsHD5DS', 'https://imgur.com/Ill3Ybg',
              'https://imgur.com/BsxBAmI', 'https://imgur.com/SvpBXEC', 'https://imgur.com/XHk4Vc8',
              'https://imgur.com/8tN0Ps4', 'https://imgur.com/4Pxeh8P', 'https://imgur.com/Oo0Sohz',
              'https://imgur.com/0X1sC7I', 'https://imgur.com/DxVDg95', 'https://imgur.com/Kms55nn',
              'https://imgur.com/olSvksZ', 'https://imgur.com/BXyIkv8', 'https://imgur.com/Pk3SONx',
              'https://imgur.com/p27Dc1Q', 'https://imgur.com/z3P793c', 'https://imgur.com/8ZkMiNN',
              'https://imgur.com/oic0TvE', 'https://imgur.com/eZCGH3i', 'https://imgur.com/kbq9XCH',
              'https://imgur.com/CKWeA8t', 'https://imgur.com/DOHsXHS', 'https://imgur.com/GMjwk2P',
              'https://imgur.com/H1f5UM5', 'https://imgur.com/eo4u2RP', 'https://imgur.com/crrHbbt',
              'https://imgur.com/2kjKShR', 'https://imgur.com/VlrcijB', 'https://imgur.com/430R77R',
              'https://imgur.com/fcMlu3K', 'https://imgur.com/u73G3NX', 'https://imgur.com/waq9Ncr',
              'https://imgur.com/S7eDPvx', 'https://imgur.com/QlFLGn7', 'https://imgur.com/b8GLzgC',
              'https://imgur.com/MKmIbda', 'https://imgur.com/JCsdBNy', 'https://imgur.com/Kdtsr7l',
              'https://imgur.com/FIaUX0t', 'https://imgur.com/BOWu3AH', 'https://imgur.com/uuk5qQK',
              'https://imgur.com/RPVhIvE', 'https://imgur.com/SW6fMvp', 'https://imgur.com/wY3rYYF',
              'https://imgur.com/y8kozO4', 'https://imgur.com/XmuDRpg', 'https://imgur.com/dl1xgis',
              'https://imgur.com/jBAbrAY', 'https://imgur.com/Z51uwWE', 'https://imgur.com/l7wsY8S',
              'https://imgur.com/Dsp8ddz', 'https://imgur.com/z6mFf5i', 'https://imgur.com/a5gDZWY',
              'https://imgur.com/k3KpL9Q', 'https://imgur.com/ZWBBD4x', 'https://imgur.com/qKCtsIV',
              'https://imgur.com/6Hx0zbK', 'https://imgur.com/Zv99huW', 'https://imgur.com/RhbOOrN',
              'https://imgur.com/Uzrihom', 'https://imgur.com/annaE7s', 'https://imgur.com/yxJ1vv8',
              'https://imgur.com/2iZzGE5', 'https://imgur.com/TbXrucH', 'https://imgur.com/rJQLcsw',
              'https://imgur.com/AslnmrQ', 'https://imgur.com/qZnwZk3', 'https://imgur.com/S9uNkRG',
              'https://imgur.com/sJkRMau', 'https://imgur.com/yA8nMxY', 'https://imgur.com/TtPzzct',
              'https://imgur.com/z7RdNKx', 'https://imgur.com/DkIRmrK', 'https://imgur.com/N8JYHMg',
              'https://imgur.com/yFW1Yzt', 'https://imgur.com/DSCHi2C', 'https://imgur.com/TGLWR5l',
              'https://imgur.com/U3OFp6y', 'https://imgur.com/vv0OtkK', 'https://imgur.com/erai55K',
              'https://imgur.com/LSQPrMy', 'https://imgur.com/mo4tUhc', 'https://imgur.com/GPYMuPy',
              'https://imgur.com/pXQ2b5n', 'https://imgur.com/uSoJoWP', 'https://imgur.com/gvSreWG',
              'https://imgur.com/ncp4UEY', 'https://imgur.com/Bw8KH5v', 'https://imgur.com/vaGlXoG',
              'https://imgur.com/cq5ngNZ', 'https://imgur.com/8DUQNvO', 'https://imgur.com/HDL01oF',
              'https://imgur.com/JTWwP6a', 'https://imgur.com/5RzoF7I', 'https://imgur.com/tNf5dXE',
              'https://imgur.com/65CXohg', 'https://imgur.com/2HaJLoy', 'https://imgur.com/fibNEwD',
              'https://imgur.com/gU4KT2W', 'https://imgur.com/uFmUV4B', 'https://imgur.com/t6eUcVh',
              'https://imgur.com/JXrTuVI', 'https://imgur.com/OkzooBd', 'https://imgur.com/Q2z9GgI',
              'https://imgur.com/wD0v7WC', 'https://imgur.com/u7j15Vn', 'https://imgur.com/th4Dpd1',
              'https://imgur.com/pBAfZR1', 'https://imgur.com/XIqnFYb', 'https://imgur.com/MSdDmM7',
              'https://imgur.com/sp2vfXp', 'https://imgur.com/dNTWXhF', 'https://imgur.com/ARWV2D5',
              'https://imgur.com/OadjIRs', 'https://imgur.com/oFhCtME', 'https://imgur.com/6UAWCSE',
              'https://imgur.com/BdNIyzP', 'https://imgur.com/As0n6W3', 'https://imgur.com/F9Bx655',
              'https://imgur.com/gvPUg4D', 'https://imgur.com/GH25dUI', 'https://imgur.com/ZGJBqHv',
              'https://imgur.com/H3IBRaO', 'https://imgur.com/GSrVLc3', 'https://imgur.com/7AaJvTX',
              'https://imgur.com/IaCHqJX', 'https://imgur.com/s6EUDF1', 'https://imgur.com/ABLep7l',
              'https://imgur.com/iwvlTXc', 'https://imgur.com/UMlNx5Q', 'https://imgur.com/GMgSJy1',
              'https://imgur.com/Ljhtxwv', 'https://imgur.com/VnwadmU', 'https://imgur.com/TNYMAbL',
              'https://imgur.com/Jj6Gag0', 'https://imgur.com/I1M7jku', 'https://imgur.com/6kEEKHM',
              'https://imgur.com/rusJ5tB', 'https://imgur.com/g76FiuD', 'https://imgur.com/zrFrhTw',
              'https://imgur.com/TITyDJ8', 'https://imgur.com/TfShNR6', 'https://imgur.com/Bpb3f2t',
              'https://imgur.com/XeAXgNL', 'https://imgur.com/N2N8akP', 'https://imgur.com/dBJukCy',
              'https://imgur.com/Tc0bLz0', 'https://imgur.com/sNlTJrM', 'https://imgur.com/qE55GXw',
              'https://imgur.com/YxxBUVw', 'https://imgur.com/auIlZuT', 'https://imgur.com/Zcmpspa',
              'https://imgur.com/arHGep4', 'https://imgur.com/m5ZLIfs', 'https://imgur.com/1QPlSx9',
              'https://imgur.com/Qnbn0lZ', 'https://imgur.com/B2fA3QW', 'https://imgur.com/K9Wcbqj',
              'https://imgur.com/cLdR4Ke', 'https://imgur.com/1zkcP34', 'https://imgur.com/CYHYDg9',
              'https://imgur.com/EC0D42V', 'https://imgur.com/gnwCUNP', 'https://imgur.com/pdrabyl',
              'https://imgur.com/AlMMgUU', 'https://imgur.com/J5TOrn4', 'https://imgur.com/F9IFkyp',
              'https://imgur.com/zMrhuYE', 'https://imgur.com/CAYHCOb', 'https://imgur.com/8Yiv3kk',
              'https://imgur.com/9miuyKJ', 'https://imgur.com/9U2rfp2', 'https://imgur.com/bUpAlC0',
              'https://imgur.com/1gIRDIb', 'https://imgur.com/kPmHJvZ', 'https://imgur.com/uKWBt5W']
emojidict = {"angular": "angular",
             "🆗": "Uczestnik"}
IDHERE = 0
#r = redis.from_url("redis://h:pfl0cfuvr58fhsduesr9kau765k@ec2-54-221-206-137.compute-1.amazonaws.com:6379")


# r=redis.Redis(host='ec2-54-75-172-124.eu-west-1.compute.amazonaws.com',port=19959,db=0,
#              password='p3b76b0fee21643a280f7c95ee5cc8218788bcf157077963081649b0f01b9e922')

'''
def openr():
    stalkingdict = {}
    for key in r.scan_iter():
        stalkingdict[key.decode("utf-8")] = r.get(key).decode("utf-8").replace(",", "").split()
    return stalkingdict
'''

# running up
@client.event
async def on_ready():
    #global stlkdict
    #stlkdict = openr()
    print('We have logged in as {0.user}'.format(client))


# entering server
@client.event
async def on_guild_join(guild):
    await guild.system_channel.send("Hello, my name is Latul\nIf anyone wants to talk just smile and ask :>")


# commands
@client.event
async def on_message(message):
    if message.content.startswith(":>"):
        if message.author.id == 449970375372046338:
            if message.content == ":>?":
                await message.delete()
                await message.channel.send("https://i.imgur.com/rGmz0YW.png")
            if message.content.lower() == ":>pyrope way":
                await message.channel.send("i.imgur.com/IGgyeIe.jpg")
            if message.content.startswith(':>kanal'):
                await message.channel.send(message.channel.id)
            if message.content.lower() == ":>roles":
                for rol in message.guild.roles:
                    print(rol, rol.id, rol.color)
            if message.content.lower() == ":>members":
                for pers in message.guild.members:
                    print(pers, pers.id, pers.roles)
                    '''
            if message.content.lower() == ':>mlem':
                print(r.get("asd"))
                print(stlkdict["asd"])
            if message.content == ":>welp":
                r.delete("asd")
                stlkdict.pop("asd")
            if message.content.lower() == ":>blep":
                r.set("asd2",message.author.mention)
                await message.channel.send(str(r.get("asd2"))[2:-1])'''
            if message.content.lower() == ':>klme':
                await message.delete()
                await message.channel.send('<:tergun:694576818019106888>' + '<:turrezi:757675153953128530>')
                '''
            if message.content == ":>MERGE":
                for key in r.scan_iter():
                    r.delete(key)
                stalkdict = openingr()
                for key in stalkdict:
                    r.set(key, str(stalkdict[key]).replace("[", "").replace("]", "").replace("'", ""))
                for key in r.scan_iter():
                    print(key, r.get(key))
            if message.content.lower().startswith(":>rdict"):
                for key in r.scan_iter():
                    print(key, r.get(key))
            if message.content.lower().startswith(":>dict"):
                for key in stlkdict:
                    print(key, stlkdict[key])'''
        if message.content.lower().startswith(':>roll'):
            throw = ''
            for chr in message.content:
                if chr.isdigit():
                    throw += chr
            result = random.randint(1, int(throw))
            await message.channel.send(result)
        if message.guild.id == 639557945364840448:
            if message.channel.id != 640297528130273290:
                if message.content == ("$m"):
                    await message.channel.send("WYPIERDALAJ")
                    '''
            if message.content.lower().startswith(":>stalker"):
                series = message.content[10:].lower()
                person = message.author.mention.replace("!", "")
                if series in stlkdict.keys():
                    if person in stlkdict[series]:
                        await message.channel.send("Już jesteś zapisan'd")
                    else:
                        stlkdict[series].append(person)
                        a = r.get(series).decode("utf-8") + ", " + person
                        r.set(series, a)
                    return 1  # rozszerzenie listy
                else:
                    stlkdict[srchkey] = [ment]
                    r.set(srchkey, ment)
                    return 1  # utworzenie listy
               fnc = openadd(series,person)
                if fnc == 1:
                    await message.channel.send("Zrobion'd")
                elif fnc == 2:
                    
                else:
                    await message.channel.send("Coś się zjebało")
            if message.content.lower().startswith(":>unstalker"):
                series = message.content[12:].lower()
                person = message.author.mention.replace("!", "")
                stlklist = list(r.get(series))
                if person in stlklist:
                    if len(stlklist) == 1:
                        r.delete(series)
                    else:
                        stlklist.pop(person)
                        r.set(series, str(stlklist))
                    await message.channel.send("Odzrobion'd")
                else:
                    await message.channel.send("Nie stalkujesz tej serii")
            if message.content.lower().startswith(":>serie"):
                person = str(message.author.mention.replace("!", ""))
                serieslist = []
                for x in stlkdict.keys():
                    # if person in r.get(key).decode("utf-8").replace(",","").split():
                    if person in stlkdict[x]:
                        serieslist.append(x)
                serieslist.sort()
                await message.channel.send(str(serieslist))'''
        if message.content.lower() == ':>help':
            await message.channel.send("Na to, co ci dolega, już nic nie pomoże")
        if message.content.lower().startswith(':>star'):
            star = random.choice(stars_list)
            await message.channel.send(star)
        if message.content.lower().startswith(':>hello') or message.content.lower().startswith(':>hey'):
            await message.channel.send('Hello :>')
        if message.content.startswith(':>AWAKE'):
            if message.author.id == 449970375372046338:
                await message.channel.send('Ph’nglui mglw’nafh Cthulhu R’lyeh wgah’nagl fhtagn', tts=True)
            else:
                await message.channel.send('Nie dla psa, dla pana to', tts=True)
        if message.content == ':>':
            await message.channel.send("Hi beautiful :>")
    '''
    if message.author.name == "Mudabutler 47":
        # print(message)
        if message.embeds:
            # for x in message.embeds[0].to_dict():
            #   print(x,"    ",message.embeds[0].to_dict()[x])
            # print(text)
            if "footer" not in message.embeds[0].to_dict():
                text = message.embeds[0].to_dict()["description"].lower().split("\n")[0]
                if text in stlkdict.keys():
                    for x in stlkdict[text]:
                        if "449970375372046338" not in x:
                            await message.channel.send(text + " " + x)'''
    if "koron" in message.content.lower() or "coron" in message.content.lower():
        await message.add_reaction("👑")
    if message.mention_everyone:
        await message.channel.send("https://i.imgur.com/rFMrQhS.mp4")
    if message.content.startswith('>:') or message.content.startswith(':<'):
        await message.channel.send("Turn that frown upside down :>")


# rainbowheart
@client.event
async def on_reaction_add(reaction, user):
    if user.bot == False:
        if reaction.emoji == "❤️":
            await reaction.message.add_reaction("🧡")
            await reaction.message.add_reaction("💛")
            await reaction.message.add_reaction("💚")
            await reaction.message.add_reaction("💙")
            await reaction.message.add_reaction("💜")


@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == IDHERE:
        rolename = emojidict[payload.emoji.name]
        role0 = discord.utils.find(lambda r: r.name == rolename, payload.member.guild.roles)
        await payload.member.add_roles(role0)


@aiocron.crontab('0,15,30,45 */1 * * * 02')
async def hsquote():
    chan = client.get_channel(640297528130273290)
    line = random.randrange(10925)
    quote = linecache.getline("hsdone.txt", line)
    await chan.send(quote)


@aiocron.crontab('0 9,14,20 * * * 02')
async def mitch():
    chan = client.get_channel(640297528130273290)
    gld = client.get_guild(639557945364840448)
    ment = gld.get_member(366466306146566144).mention
    await chan.send("https://i.imgur.com/RYyzqU2.gif")
    await chan.send(ment)


@aiocron.crontab('0 9,21 * * * 02')
async def ter():
    chan = client.get_channel(640297528130273290)
    gld = client.get_guild(639557945364840448)
    ment = gld.get_member(291474953143058432).mention
    await chan.send("https://i.imgur.com/RYyzqU2.gif")
    await chan.send(ment)


@aiocron.crontab('0 8,20 * * * 02')
async def eri():
    chan = client.get_channel(640297528130273290)
    gld = client.get_guild(639557945364840448)
    ment = gld.get_member(303571655526187009).mention
    await chan.send("https://i.imgur.com/RYyzqU2.gif")
    await chan.send(ment)


client.run(TOKEN)