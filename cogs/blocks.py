from discord.ext import commands

class BlocksCog(commands.Cog, name="Blocks"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='blocks', help="Displays summary of block information")
    async def block(self,ctx):
        try:
            value = await self.bot.send_rpc({"action":"block_count"},"count")
            blockCount = int(value)
            cementedBlocks = await self.bot.send_rpc({"action":"block_count"},"cemented")
            cemented = int(cementedBlocks)
            uncheckedBlocks = await self.bot.send_rpc({"action":"block_count"},"unchecked")
            sync = float(cemented/blockCount)
            response = (
                f"**Cemented Blocks:** {cementedBlocks}\n"
                f"**Block Count:** {blockCount}\n"
                f"**Unchecked Blocks:** {uncheckedBlocks}\n"
                f"**Sync:**: {sync:.4f}%\n"
            )
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab blocks", e)       

    @commands.command(name='current_block', aliases=['currentblock','cur','current'], help="Displays the current block")
    async def current_block(self,ctx):
        try:
            value = await self.bot.send_rpc({"action":"block_count"},"count")
            response = f"Current block is {value}"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab current_block", e)     

    @commands.command(name='cemented_blocks', aliases=['cementedblocks','cemented','cem'], help="Displays the cemented block count")
    async def cemented_blocks(self,ctx):
        try:
            value = await self.bot.send_rpc({"action":"block_count"},"cemented")
            response = f"Cemented block count is {value}"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab cemented_blocks", e)  

    @commands.command(name='unchecked_blocks', aliases=['uncheckedblocks','unchecked'], help="Displays the number of unchecked blocks")
    async def unchecked_blocks(self,ctx):
        try:
            value = await self.bot.send_rpc({"action":"block_count"},"unchecked")
            response = f"{value} unchecked blocks"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab unchecked blocks", e)   

    @commands.command(name='sync', aliases=['blocksync','block_sync','bsync'], help="Displays block sync")
    async def block_sync(self,ctx):
        try:
            value = await self.bot.send_rpc({"action":"block_count"},"cemented")
            cemented = int(value)
            value = await self.bot.send_rpc({"action":"block_count"},"count")
            blockCount = int(value)
            sync = float(cemented/blockCount)
            response = f"Block sync is {sync:.4f}%"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab sync", e)  

# Plug-in function to add cog
def setup(bot):
    bot.add_cog(BlocksCog(bot))
