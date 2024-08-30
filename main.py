from asyncio import LimitOverrunError
import time as t
import discord
from pypresence import Presence
from humanfriendly import parse_timespan,InvalidTimespan
import datetime
from typing import Optional,Callable
from discord.ext import commands
from discord import app_commands,Interaction, Member , user , utils as Utils,TextChannel
import discord.ext
import time as t
#-------------------------------------Import---------------------------------------#
Bot = commands.Bot(command_prefix= "." , intents= discord.Intents.all())
#--------------------------------------------------Commands-------------------------------------------------------#


@Bot.command()
async def yardım(ctx):
    embed = discord.Embed(title="Komutlar",description="**.Sa**\nBu Komut Kişiye Selam Verir\n**.sil**\nBu Komut Belirlediğiniz Sayıdaki Mesajları Siler\n**.ip**\nBu KomutSunucunun Bilgileri Öğrenmenize Yardımcı Olur\n**.Kick**\nBu Komut Sunucudaki Kişiyi Çıkartır\n**.Ban**\nBu Komut Sunucudaki Kişiyi Banlamanızı Sağlar\n**.UnBan**\nSunucudaki Banlı Bir Kişinin Banını Kaldırır\n**.Dc**\nBu Komut Discordu Öğrenmenizi Sağlar\n**.lock**\nBu Komut Kanalı Kitlemenizi Sağlar\n**.unlock**\nBu Komut Kanalın Kilidinin Açılmasını Sağlar\n**.mute**\nBu Komut Kişiye Zaman Aşımı Atar\n**.unmute**\nBu Komut Kişinin Zaman Aşımını Kaldırır",color= discord.Colour.blue(),timestamp=datetime.datetime.now())   
    await ctx.send(embed=embed)


@Bot.tree.command(name="yardım", description="Bu Komut Size Bot Hakkında Yardımcı Olur")
async def yardım(interaction=discord.Interaction):
    await interaction.response.send_message(f"Bilgi Almak İstiyorsan **.yardım** komudunu girmelisin {interaction.user.mention}",
    ephemeral=True)
    

@Bot.command()
async def sa(ctx):
    await ctx.send(f"Aleyküm Selam Hoş Geldin")
    
@Bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    channel = ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role,overwrite=overwrite)
    embed = discord.Embed(title="🔒Lock",description=f"Bu kanal **{ctx.author.name}** tarafından kitlendi.", color=discord.Colour.red(),timestamp=datetime.datetime.now())
    await ctx.send(embed=embed)

@Bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    channel = ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role,overwrite=overwrite)
    embed = discord.Embed(title="🔒UnLock",description=f"Bu kanal **{ctx.author.name}** tarafından kilidi açıldı.", color=discord.Colour.green(),timestamp=datetime.datetime.now())
    await ctx.send(embed=embed)

@Bot.command()
@commands.has_permissions()
async def mute(ctx,member: discord.Member,timelimit):
    if "s" in timelimit:
        gettime =  timelimit.strip("s")
        newtime = datetime.timedelta(seconds=int(gettime))
        await member.edit(timed_out_until=discord.utils.utcnow()+ newtime)
        embed = discord.Embed(title="Zaman Aşımı",description=f"**{member}** Adlı Kişiye Zaman Aşımı Uygulandı\n**Süre**:{newtime}\n**Yetkili:** {ctx.author.name}:",timestamp=datetime.datetime.now())
        await ctx.send(embed=embed)
    if "m" in timelimit:
        gettime =  timelimit.strip("m")
        newtime = datetime.timedelta(minutes=int(gettime))
        await member.edit(timed_out_until=discord.utils.utcnow()+ newtime)
        embed = discord.Embed(title="Zaman Aşımı",description=f"**{member}** Adlı Kişiye Zaman Aşımı Uygulandı\n**Süre**:{newtime}\n**Yetkili:** {ctx.author.name}:",timestamp=datetime.datetime.now())
        await ctx.send(embed=embed)
    if "h" in timelimit:
        gettime =  timelimit.strip("h")
        newtime = datetime.timedelta(hours=int(gettime))
        await member.edit(timed_out_until=discord.utils.utcnow()+ newtime)
        embed = discord.Embed(title="Zaman Aşımı",description=f"**{member}** Adlı Kişiye Zaman Aşımı Uygulandı\n**Süre**:{newtime}\n**Yetkili:** {ctx.author.name}:",timestamp=datetime.datetime.now())
        await ctx.send(embed=embed)
    if "d" in timelimit:
        gettime =  timelimit.strip("d")
        newtime = datetime.timedelta(days=int(gettime))
        await member.edit(timed_out_until=discord.utils.utcnow()+ newtime)
        embed = discord.Embed(title="Zaman Aşımı",description=f"**{member}** Adlı Kişiye Zaman Aşımı Uygulandı\n**Süre**:{newtime}\n**Yetkili:** {ctx.author.name}",timestamp=datetime.datetime.now())
        await ctx.send(embed=embed)


@Bot.command()
@commands.has_permissions(moderate_members=True)
async def unmute(ctx,member: discord.Member):
    await member.edit(timed_out_until=None)
    embed = discord.Embed(title="Zaman Aşımı",description=f"**{member}** Adlı Kişinin Zaman Aşımı Kaldırıldı",color = discord.Colour.dark_green(),timestamp=datetime.datetime.now())
    await ctx.send(embed=embed)


@Bot.command()
async def ip(ctx):
    ip = "**oyna.RionMC.Com.Tr**"
    embed = discord.Embed(title="Bilgilendirme",description=f"Sunucumuzu ip'si {ip}\nHerkesi Bekleriz :)", color = discord.Colour.green(),timestamp=datetime.datetime.now())
    await ctx.send(embed=embed)


@Bot.command(aliases = ["purge","delete","clear"])
@commands.has_permissions(manage_messages=True)
async def sil(ctx,amount: int):
    if amount < 1:
        embed = discord.Embed(title="Hata",description=f"\n**Komutu Çalıştırırken Bir Hata Oluştu**", color = discord.Colour.red(),timestamp=datetime.datetime.now())
        await ctx.send(embed=embed)
        
    else:
        await ctx.channel.purge(limit=amount+1)
        embed = discord.Embed(title="Sil",description=f"**Başarıyla {amount} tane mesaj silindi**", color=discord.Colour.green(),timestamp=datetime.datetime.now())
        await ctx.send(embed=embed)
        
@Bot.command()
@commands.has_permissions(manage_channels=True)
async def kanalsil(ctx,channel: discord.TextChannel):
    embed = discord.Embed(
        title="Kanal Sil",
        description=f"**{channel}** Adlı Kanal Başarıyla silindi",
        color=discord.Colour.green()
    )
    if ctx.author.guild_permissions.manage_channels:
        if channel == discord.TextChannel:
            await ctx.send(embed=embed)
            await channel.delete()

    



@Bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member: discord.Member,* ,reason = None):
    embed = discord.Embed(title="Kick",description=f"**{member}** Adlı Kişi Başarıyla Atıldı\n**Sebep**: {reason}", color = discord.Colour.green(),timestamp=datetime.datetime.now())
    await member.kick(reason=reason)
    await ctx.send(embed=embed)

@Bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member: discord.Member,* ,reason = None):
    await member.ban(reason=reason)
    embed = discord.Embed(title="Ban",description=f"**Banned:** {member}\n**Reason:** {reason}", color = discord.Colour.dark_red())
    await ctx.send(embed=embed)

@Bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,user: discord.User):
    guild = ctx.guild
    embed = discord.Embed(
        title="Unban",
        description=f"**{user}** Adlı Kişinin Banı Başarıyla Kaldırıldı",
        color= discord.Colour.green()
    )
    if ctx.author.guild_permissions.ban_members:
        await ctx.send(embed=embed)
        await guild.unban(user=user)

@Bot.command()
async def dc(ctx,member: discord.Member = None):
    icon = "https://images-ext-2.discordapp.net/external/gAuBm_HY8VWxGtbMAEjKHkS0tW5vcnXInMNRGsvkd-c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1200434757889179648/5e52b3f48650078b23a695cfe3813ddf.png?format=webp&quality=lossless&width=638&height=638"
    embed = discord.Embed(title="Discord",description="**Discordumuza Katılmak ister misin?\n   ↓Hemen Buna Tıkla↓\n**      [Discord](https://discord.gg/D62d3YdwTa)")
    embed.set_thumbnail(url=f"{icon}")
    await ctx.send(embed=embed)

@Bot.command()
async def say(ctx,*,message):
    await ctx.message.delete()
    await ctx.send(message)

        



#--------------------------------------------------Events-------------------------------------------------------#
#                                                                                                               #
#                                                                                                               #
#--------------------------------------------------Events-------------------------------------------------------#
@Bot.event
async def on_command_error(ctx,error):
    missing_permission_embed = discord.Embed(
        title="Error",
        description="**Bunu Yapmak İçin Yetkin Yok**",
        color=discord.Colour.red()
    )
    CommandInvokeError_embed = discord.Embed(
        title="Error",
        description="**Bu Kişi Senden Üstün**",
        color=discord.Colour.red()
    )
    MissingRequiredArgument_embed = discord.Embed(
        title="Error",
        description="**Bir Şeyi Eksik Yazmışsın Gibi Görünüyor**",
        color=discord.Colour.red()
    )
    embed = discord.Embed(title="ERROR",description=f"\n**Komutu Çalıştırırken Bir Hata Oluştu**", color = discord.Colour.red())
    if isinstance(error,commands.errors.CommandInvokeError):
        await ctx.send(embed=CommandInvokeError_embed)
        print(error,commands.errors.CommandInvokeError)
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(embed=MissingRequiredArgument_embed)
        print(error,commands.MissingRequiredArgument)
    if isinstance(error,commands.MissingPermissions):
        await ctx.send(embed=missing_permission_embed)
        print(error,commands.MissingPermissions)


@Bot.event
async def on_ready():
    print("Bot Başarılı Bir Şekilde Açıldı")
    await Bot.change_presence(
    status=discord.Status.dnd,
    activity=discord.activity.CustomActivity("Working"))
    try:
        synced = await Bot.tree.sync()
        print(f"Synced{len(synced)} commands")
    except Exception as e:
        print(e)



    





























































#-----Run-----#
Bot.run("TOKEN")
