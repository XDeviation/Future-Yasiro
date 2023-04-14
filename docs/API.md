# Future Yasiro API doc

At first, you should know how Future Yasiro run.

Future Yasiro has split in 3 modules, receive module, send module and plugin.

Receive module will listen a port, which receive go-cqhttp message and send message to mq

Send module will consume the queue "message", and send all message to where it need to send.

Plugins consume it self mq, such as "ping", and send message to "message" queue.