
import socket
from discord.ext import commands
from common import Common
import psutil
import time

class ServerCog(commands.Cog, name="Server"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='server', help="Displays summary of server information")
    async def server(self,ctx):
        try:
            server_load =  psutil.cpu_percent()
            usedMem = psutil.virtual_memory().used / 1e6
            totalMem = psutil.virtual_memory().total / 1e6
            percent = int(usedMem) / int(totalMem) * 100
            seconds = time.time() - psutil.boot_time()
            server_uptime = Common.get_days_from_secs(seconds)
            value = await self.bot.send_rpc({"action": "uptime"},"seconds")
            pretty_node_uptime = Common.get_days_from_secs(int(value))
            server = socket.gethostname()
            ip_addr = socket.gethostbyname(server)
            response = (
                f"**Server:** {server} [{ip_addr}]\n"
                f"**Server Load:** {server_load}\n"
                f"**Memory Usage:** {usedMem:.2f} MB / {totalMem:.2f} MB : {percent:.2f}%\n"
                f"**Server Uptime:** {server_uptime}\n"
                f"**Node Uptime:** {pretty_node_uptime}"
            )
            await ctx.send(response)
        except Exception as e:
            raise Exception("Exception displaying server summary", e)      

    @commands.command(name='server_uptime', aliases=['serveruptime','sup'], help="Displays server uptime")
    async def server_uptime(self,ctx):
        try:
            seconds = time.time() - psutil.boot_time()
            server_uptime = Common.get_days_from_secs(seconds)
            response = f"Server uptime is {server_uptime}"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab server_uptime", e)      

    @commands.command(name='server_load', aliases=['serverload','systemload','load'], help="Displays server load")
    async def server_load(self,ctx):
        try:
            server_load =  psutil.cpu_percent()
            response = f"Server load is {server_load}"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab server_load", e)           

    @commands.command(name='mem_usage', aliases=['memory_usage','memusage','memory','mem'], help="Displays memory usage")
    async def mem_usage(self,ctx):
        try:

            usedMem = psutil.virtual_memory().used / 1e6
            totalMem = psutil.virtual_memory().total / 1e6
            percent = int(usedMem) / int(totalMem) * 100
            response = f"Memory usage is {usedMem} MB / {totalMem} MB : {percent:.2f}%"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab mem_usage", e)      

    @commands.command(name='hostname', aliases=['host'], help="Displays host name")
    async def node_name(self,ctx):
        try:
            value = socket.gethostname()
            response = f"Node hostname is {value}"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab host name", e)      

# Plug-in function to add cog
def setup(bot):
    bot.add_cog(ServerCog(bot))