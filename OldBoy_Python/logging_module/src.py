# 接下来要做的是：拿到日志的产生者即loggers来产生日志
# 第一个日志产生者：随便起名
# 第二个日志产生者：专门的采集

# 但是需要先导入日志配置字典LOGGING_DIC
import settings

# !!!强调!!!
# 1、logging是一个包，需要使用其下的config、getLogger，可以如下导入
# from logging import config
# from logging import getLogger

# 2、也可以使用如下导入
import logging.config    # 这样连同logging.getLogger都一起导入了,然后使用前缀logging.config.

# 3、加载配置
logging.config.dictConfig(settings.LOGGING_DIC)

# 4、输出日志
logger1 = logging.getLogger('随便起名')
logger1.info('egon儿子alex转账3亿冥币')

logger2=logging.getLogger('专门的采集') # 名字传入的必须是'专门的采集'，与LOGGING_DIC中的配置唯一对应
logger2.debug('专门采集的日志')
