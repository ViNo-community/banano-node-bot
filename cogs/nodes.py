from discord.ext import commands
from common import Common

class NodesCog(commands.Cog, name="Nodes"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='node', help="Displays summary of node information")
    async def node(self,ctx):
        try:
            account = await self.bot.get_banano_account()
            # Get node version
            version = await self.bot.send_rpc({"action":"version"},"node_vendor")
            # Get number of network pairs
            peers = await self.bot.send_rpc({"action":"peers"},"peers")
            peerCount = len(peers)
            response = (
                f"**Address:** {account}\n"
                f"**Version:** {version}\n"
                f"**Number of Peers:**: {peerCount}\n"
            )
            await ctx.send(response)
        except Exception as e:
            raise Exception("Error showing node summary", e)    

    @commands.command(name='address', aliases=['addr','node_address','nodeaddress'], help="Displays node address")
    async def address(self,ctx):
        try:
            account = await self.bot.get_banano_account()
            response = f"Banano node address is {value}"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab address", e)  

    @commands.command(name='version', aliases=['ver'], help="Displays node version")
    async def version(self,ctx):
        try:
            value = await self.bot.send_rpc({"action":"version"},"node_vendor")
            response = f"Node version is {value}"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not show version", e)

    @commands.command(name='peers', help="Displays peers")
    async def peers(self,ctx):
        try:
            # Get number of network pairs
            peers = await self.bot.send_rpc({"action":"peers"},"peers")
            peerCount = len(peers)
            msg = ""
            i = 0
            CHUNK_SIZE = 1000
            for peer in peers:
                i = i + 1
                # Cut message into chunks
                if(len(msg) > self.bot.DISCORD_MAX_MSG_LEN):
                    await ctx.send(msg)
                    msg = ""
                msg += f"**Peer #{i}:** {peer}\n"
            msg += f"{peerCount} peers"
            await ctx.send(msg)
        except Exception as e:
            raise Exception("Could not grab num_peers", e)   

    @commands.command(name='uptime', aliases=['up','nodeuptime','node_uptime'], help="Displays node uptime")
    async def uptime(self,ctx):
        try:
            value = await self.bot.send_rpc({"action": "uptime"},"seconds")
            pretty_node_uptime = Common.get_days_from_secs(int(value))
            response = f"Node uptime is {pretty_node_uptime}"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab uptime", e)   

# Plug-in function to add cog
def setup(bot):
    bot.add_cog(NodesCog(bot))
