import asyncio

from selfcord import Bot, Context, Extender


class Ext(
    Extender,
    name="Unix",
    description="CLI related commands here. Majority won't work unless the given program is installed. Used from a linux operating system.",
):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

    @Extender.cmd(description="NMAP command")
    async def nmap(self, ctx: Context, *, msg: str):
        """The NMAP command, equivalent to nmap CLI tool. Does not require root permissions. Requires privileges for nmap."""
        val = await asyncio.subprocess.create_subprocess_shell(
            "nmap --privileged " + msg,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await val.communicate()
        if stdout:
            if len(stdout.decode()) < 1800:
                msg = f"```ini\n[ STDOUT ]\n{stdout.decode()}```"
                await ctx.reply(msg, delete_after=60)
            else:
                for i in range(0, len(stdout.decode()), 1800):
                    msg = f"```ini\n[ STDOUT ]\n{stdout.decode()[i:i+1800]}```"
                    await ctx.reply(msg, delete_after=60)
                    await asyncio.sleep(1.5)

        if stderr:
            if len(stderr.decode()) < 1800:
                msg = f"[ STDERR ]\n{stderr.decode()}"
            else:
                for i in range(0, len(stderr.decode()), 1800):
                    msg = f"```ini\n[ STDERR ]\n{stderr.decode()[i:i+1800]}"
                    await ctx.reply(msg, delete_after=60)
                    await asyncio.sleep(1.5)


    @Extender.cmd(
        description="Nslookup command. Gathers information on a domain/ip address"
    )
    async def nslookup(self, ctx: Context, *, msg):
        """The Nslookup coomand, equivalent to the nslookup cli tool. Does not require root permissions. Shows IP address related to domains and dns records."""
        val = await asyncio.subprocess.create_subprocess_shell(
            "nslookup " + msg,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await val.communicate()
        if stdout:
            if len(stdout.decode()) < 1800:
                msg = f"```ini\n[ STDOUT ]\n{stdout.decode()}```"
                await ctx.reply(msg, delete_after=60)
            else:
                for i in range(0, len(stdout.decode()), 1800):
                    msg = f"```ini\n[ STDOUT ]\n{stdout.decode()[i:i+1800]}```"
                    await ctx.reply(msg, delete_after=60)
                    await asyncio.sleep(1.5)

        if stderr:
            if len(stderr.decode()) < 1800:
                msg = f"[ STDERR ]\n{stderr.decode()}"
            else:
                for i in range(0, len(stderr.decode()), 1800):
                    msg = f"```ini\n[ STDERR ]\n{stderr.decode()[i:i+1800]}"
                    await ctx.reply(msg, delete_after=60)
                    await asyncio.sleep(1.5)

    @Extender.cmd(description="Curl command. Gather data from apis/domains.")
    async def curl(self, ctx: Context, *, msg):
        """The curl command. equivalent to the curl cli tool. Does not require root permissions. Gathers data from api endpoints or domains, can be used to test these api links."""
        val = await asyncio.subprocess.create_subprocess_shell(
            "curl " + msg,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await val.communicate()
        if stdout:
            if len(stdout.decode()) < 1800:
                msg = f"```ini\n[ STDOUT ]\n{stdout.decode()}```"
                await ctx.reply(msg, delete_after=60)
            else:
                for i in range(0, len(stdout.decode()), 1800):
                    msg = f"```ini\n[ STDOUT ]\n{stdout.decode()[i:i+1800]}```"
                    await ctx.reply(msg, delete_after=60)
                    await asyncio.sleep(1.5)

        if stderr:
            if len(stderr.decode()) < 1800:
                msg = f"[ STDERR ]\n{stderr.decode()}"
            else:
                for i in range(0, len(stderr.decode()), 1800):
                    msg = f"```ini\n[ STDERR ]\n{stderr.decode()[i:i+1800]}"
                    await ctx.reply(msg, delete_after=60)
                    await asyncio.sleep(1.5)

    @Extender.cmd(description="Ping command. Pings an address to see if is online")
    async def ping(self, ctx: Context, addr: str):
        """The ping command, equivalent to the ping cli tool. Does not require root permissions. Attempts to check whether the host is online"""
        val = await asyncio.subprocess.create_subprocess_shell(
            f"ping -c 3 {addr}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await val.communicate()
        if stdout:
            if len(stdout.decode()) < 1800:
                msg = f"```ini\n[ STDOUT ]\n{stdout.decode()}```"
                await ctx.reply(msg, delete_after=60)
            else:
                for i in range(0, len(stdout.decode()), 1800):
                    msg = f"```ini\n[ STDOUT ]\n{stdout.decode()[i:i+1800]}```"
                    await ctx.reply(msg, delete_after=60)
                    await asyncio.sleep(1.5)

        if stderr:
            if len(stderr.decode()) < 1800:
                msg = f"[ STDERR ]\n{stderr.decode()}"
            else:
                for i in range(0, len(stderr.decode()), 1800):
                    msg = f"```ini\n[ STDERR ]\n{stderr.decode()[i:i+1800]}"
                    await ctx.reply(msg, delete_after=60)
                    await asyncio.sleep(1.5)
