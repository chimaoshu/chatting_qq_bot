from nonebot import on_command, CommandSession
import getAPI

# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('chat',aliases=('小小冰'))
async def chat(session: CommandSession):

    # # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    message = session.state.get('message')

    return_message = await get_return_message(message)

    await session.send(return_message)


@chat.args_parser
async def _(session: CommandSession):

    session.state['message'] = session.current_arg_text



async def get_return_message(massage: str) -> str:

    return_message = getAPI.get_content(massage)

    return return_message