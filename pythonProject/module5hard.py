class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        new_account = User(nickname, password, age)
        if self.users is []:
            self.users.append(new_account)
            self.current_user = new_account.nickname
        else:
            for i in self.users:
                if new_account.nickname == i.nickname:
                    print('Пользователь ', i.nickname, ' уже существует')
                    return self
            self.users.append(new_account)
            self.current_user = new_account.nickname
        return self

    def login(self, nickname, password):
        for i in self.users:
            if i[0] == nickname and i[1] == hash(password):
                self.current_user = i[0]
                break
            else:
                print('Пользователя с данным паролем не существует')
        return self

    def log_out(self):
        self.current_user = None
        return self

    def add(self, *args):
        check_video = False
        for i in args:
            video = [i.title, i.duration, i.time_now, i.adult_mode]
            if self.videos == []:
                self.videos.append(video)
            else:
                for j in self.videos:
                    if i.title != j[0]:
                        check_video = True
                        break
                    else:
                        check_video = False
                if check_video is True:
                    self.videos.append(video)
        return self

    def get_videos(self, find_string):
        my_list = []
        for i in self.videos:
            if i[0].lower().find(find_string.lower()) != -1:
                my_list.append(i[0])
        return my_list

    def watch_video(self, name_video):
        import time
        for i in self.videos:
            if name_video == i[0]:
                if self.current_user is None:
                    print('Войдите в аккаунт, чтобы смотреть видео')

                else:
                    for j in self.users:
                        if j.nickname == self.current_user:
                            if j.age >= 18:
                                for k in range(i[1]):
                                    i[2] = k+1
                                    print(i[2], end=' ')
                                    time.sleep(1)
                                print('Конец видео')
                            else:
                                print('Вам нет 18 лет, пожалуйста покиньте страницу')
        return self


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
