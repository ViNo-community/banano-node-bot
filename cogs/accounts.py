from discord.ext import commands
import json

from common import Common 

class AccountsCog(commands.Cog, name="Accounts"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='account', aliases=['acc'], help="Displays summary of account information")
    async def account(self,ctx):
        try:
            account = await self.bot.get_banano_account()
            representative = await self.bot.send_rpc({"action":"account_representative","account":account},"representative")
            value = await self.bot.send_rpc({"action":"account_balance","account":account},"balance")
            balance = float(Common.rawToBanano(int(value)))
            value = await self.bot.send_rpc({"action":"account_balance","account":account},"pending")
            pending = float(Common.rawToBanano(int(value)))
            value = await self.bot.send_rpc({"action":"account_weight","account":account},"weight")
            voting_weight = float(Common.rawToBanano(int(value)))
            response = (
                f"**Account:** {account}\n"
                f"**Representative:** {representative}\n"
                f"**Balance:** {balance:.2f} ban\n"
                f"**Pending:**: {pending: .2f} ban\n"
                f"**Voting Weight**: {voting_weight: .2f} ban"
            )
            await ctx.send(response)
        except Exception as e:
            raise Exception("Error showing account summary", e)      

    @commands.command(name='balance', aliases=['bal','show_balance'], help="Displays account balance")
    async def balance(self,ctx):
        try:
            account = await self.bot.get_banano_account()
            value = await self.bot.send_rpc({"action":"account_balance","account":account},"balance")
            balance = float(Common.rawToBanano(int(value)))
            response = f"Account balance is {balance:.2f} ban"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab balance", e)   

    @commands.command(name='pending', aliases=['show_pending'], help="Displays account pending")
    async def pending(self,ctx):
        try:
            account = await self.bot.get_banano_account()
            value = await self.bot.send_rpc({"action":"account_balance","account":account},"pending")
            pending = float(value)
            response = f"Account pending is {pending:.2f} ban"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not display account pending", e)     

    @commands.command(name='representative', aliases=['rep','show_rep','show_representative'], help="Displays representative")
    async def representative(self,ctx):
        try:
            account = await self.bot.get_banano_account()
            value = await self.bot.send_rpc({"action":"account_representative","account":account},"representative")
            response = f"Representative: {value}"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab representative", e)    

    @commands.command(name='voting_weight', aliases=['votingweight','weight','voting'], help="Displays voting weight")
    async def voting_weight(self,ctx):
        try:
            account = await self.bot.get_banano_account()
            value = await self.bot.send_rpc({"action":"account_weight","account":account},"weight")
            weight = float(value)
            response = f"Voting weight is {weight:.2f} ban"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab voting weight", e)  
    
    @commands.command(name='delegators_count', help="Displays the amount of delegators of the node")
    async def delegators_count(self,ctx,ref_account=""):
        try:
            # If no account specified use account of node
            if(ref_account == ""):
                banano_account = await self.bot.get_banano_account()
            else:
                banano_account = ref_account
            value = await self.bot.send_rpc({"action":"delegators_count","account":banano_account},"count")
            response = f"{banano_account} has {value} delegators"
            await ctx.send(response)
        except Exception as e:
            raise Exception("Could not grab delegators_count", e)

    @commands.command(name='delegators', aliases=['show_delegators'], help="Displays the delegators of the node")
    async def delegators(self,ctx,ref_account=""):
        try:
            # If no account specified use account of node
            if(ref_account == ""):
                banano_account = await self.bot.get_banano_account()
            else:
                banano_account = ref_account
            value = await self.bot.send_rpc({"action":"delegators","account":banano_account})
            content = json.loads(value)
            # Parse delegators information - account number and balance
            delegators = content['delegators']
            msg = ""
            if(content['delegators'] == ""):
                msg = "No delegators"
            else:
                print("delegators: ")
                for item in delegators:
                    # Convert from raw to banano
                    ban = Common.rawToBanano(int(delegators[item]))
                    # Cut message into chunks
                    if(len(msg) > self.bot.DISCORD_MAX_MSG_LEN):
                        await ctx.send(msg)
                        msg = ""
                    # Hide zero balances
                    if(ban != 0): 
                        msg += "**Account:** " + item + f" **Balance:** {ban:.4f}\n"
            await ctx.send(msg)
        except Exception as e:
            raise Exception("Could not grab delegators", e)

# Plug-in function to add cog
def setup(bot):
    bot.add_cog(AccountsCog(bot))
