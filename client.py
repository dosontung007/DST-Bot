import decline_invt
import getlink
import wish_id_user
import bot_time_table

from threading import Thread
from fbchat import log, Client
from fbchat.models import ThreadType
import time

import login_main_acc
import login_clone_acc


class Main_Bot(Client):
    def onMessage(self, author_id, thread_id, thread_type, message, **kwargs):
        def log(self, author_id, thread_id, thread_type, message, **kwargs):
            report = '''{}
                     Message from {} in {} ({}): {}
                     '''.format(time.strftime("%a, %d %b %Y %H:%M:%S"),
                                author_id, thread_id, thread_type.name,
                                message)

            log.info(report)
        if author_id != self.uid and author_id != login_clone_acc.id_:
            if thread_type.name == 'USER':
                msg_rep = decline_invt.rep_msg(message)

                if type(msg_rep) is str:
                    self.sendMessage(msg_rep,
                                     thread_id=thread_id,
                                     thread_type=thread_type)

                    log.info('Declined invitation from {}'.format(author_id))

    def good_night(self):
        t0 = time.time()

        data = wish_id_user.choose_wish()

        for i in data:
            log.info('Send message to {}'.format(i[0]))

            self.sendMessage(i[1],
                             thread_id=id,
                             thread_type=ThreadType.USER)

            self.sendMessage('Được gửi từ Good Night-Bot with <3',
                             thread_id=id,
                             thread_type=ThreadType.USER)

        t1 = time.time()

        log.info('Message delivered to {} people in {}s'.format(
            len(wish_id_user.friend_list), t1 - t0))

        print('I\'m done my job. Good night my boss')

        log.info('All wish are delivered in {}s'.format(t1 - t0))


class Clone_Bot(Client):
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        def log(self, author_id, thread_id, thread_type, message, **kwargs):
            report = '''{}
            Message from {} in {} ({}): {}
            '''.format(time.strftime("%a, %d %b %Y %H:%M:%S"),
                       author_id, thread_id, thread_type.name, message)
            log.info(report)

        if author_id != self.uid:
            message = message.lower()

            if message == 'tinhte':
                title_n_link, url_src = getlink.tinhte()
                self.sendMessage('5 bài nổi bật trên Tinhte.vn',
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                for i in range(5):
                    self.sendMessage(title_n_link[i][0],
                                     thread_id=thread_id,
                                     thread_type=thread_type)
                    self.sendRemoteImage(url_src[i],
                                         thread_id=thread_id,
                                         thread_type=thread_type)
                    self.sendMessage(title_n_link[i][1],
                                     thread_id=thread_id,
                                     thread_type=thread_type)

            if message == 'pornhub':
                title_n_link, url_src = getlink.pornhub()
                self.sendMessage('5 bộ phim nổi bật trên pornohub.su',
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                for i in range(5):
                    self.sendMessage(title_n_link[i][0],
                                     thread_id=thread_id,
                                     thread_type=thread_type)

                    self.sendRemoteImage(url_src[i],
                                         thread_id=thread_id,
                                         thread_type=thread_type)

                    self.sendMessage(title_n_link[i][1],
                                     thread_id=thread_id,
                                     thread_type=thread_type)

            if message == 'pe':
                num_n_content = getlink.PE()

                self.sendMessage('Problem ' + str(num_n_content[0]),
                                 thread_id=thread_id,
                                 thread_type=thread_type)

                self.sendMessage(num_n_content[1],
                                 thread_id=thread_id,
                                 thread_type=thread_type)

            if message == 'fml':
                title_n_link = getlink.fml()
                msg_rep = str(title_n_link[0]) + '\n' + str(title_n_link[1])

                self.sendMessage('Bài mới nhất trên FAMILUG',
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                self.sendMessage(msg_rep,
                                 thread_id=thread_id,
                                 thread_type=thread_type)

            if message == 'kenh14':
                title_n_link, url_src = getlink.kenh14()

                self.sendMessage('5 bài viết nổi bật trên kênh14',
                                 thread_id=thread_id,
                                 thread_type=thread_type)

                for i in range(5):
                    self.sendMessage(title_n_link[i][0],
                                     thread_id=thread_id,
                                     thread_type=thread_type)

                    self.sendRemoteImage(url_src[i],
                                         thread_id=thread_id,
                                         thread_type=thread_type)

                    self.sendMessage(title_n_link[i][1],
                                     thread_id=thread_id,
                                     thread_type=thread_type)

            if message == 'genk':
                title_n_link, url_src = getlink.genk()

                self.sendMessage('5 bài viết nổi bật trên Genk.vn',
                                 thread_id=thread_id,
                                 thread_type=thread_type)

                for i in range(5):
                    self.sendMessage(title_n_link[i][0],
                                     thread_id=thread_id,
                                     thread_type=thread_type)

                    self.sendRemoteImage(url_src[i],
                                         thread_id=thread_id,
                                         thread_type=thread_type)

                    self.sendMessage(title_n_link[i][1],
                                     thread_id=thread_id,
                                     thread_type=thread_type)

            if message == 'xkcd':
                data = getlink.xkcd()

                self.sendMessage('Bài viết mới nhất trên xkcd.com',
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                self.sendMessage(data[0],
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                self.sendRemoteImage(data[1],
                                     thread_id=thread_id,
                                     thread_type=thread_type)
                self.sendMessage(data[2],
                                 thread_id=thread_id,
                                 thread_type=thread_type)

            if message == 'good night':
                Main_Bot.good_night()

            if 'tkb' in message or 'Thời khóa biểu' in message:
                rep_message_ = bot_time_table.rep_message(message)

                self.sendMessage(rep_message_,
                                 thread_id=thread_id,
                                 thread_type=thread_type)

            if message == 'viettlot':
                data = getlink.viettlot()
                rep_message_ = '{}. \n'.format(data[0]) + \
                               'Số trúng Jackpot là {} \n'.format(data[1]) + \
                               'Giá trị Jackpot là {}'.format(data[2])

                self.sendMessage(rep_message_,
                                 thread_id=thread_id,
                                 thread_type=thread_type)

            if message == 'vnex':
                title_n_link, url_src = getlink.vnexpress()

                self.sendMessage('5 bài viết nổi bật trên Vnexpress',
                                 thread_id=thread_id,
                                 thread_type=thread_type)

                for i in range(5):
                    self.sendMessage(title_n_link[i][0],
                                     thread_id=thread_id,
                                     thread_type=thread_type)

                    self.sendRemoteImage(url_src[i],
                                         thread_id=thread_id,
                                         thread_type=thread_type)

                    self.sendMessage(title_n_link[i][1],
                                     thread_id=thread_id,
                                     thread_type=thread_type)


def run_main_bot():
    main_client = Main_Bot(login_main_acc.username,
                           login_main_acc.password)
    main_client.listen()


def run_clone_bot():
    clone_client = Clone_Bot(login_clone_acc.username,
                             login_clone_acc.password)
    clone_client.listen()


if __name__ == '__main__':
    Thread(target=run_main_bot).start()
    Thread(target=run_clone_bot).start()
