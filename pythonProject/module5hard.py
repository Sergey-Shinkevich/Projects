class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return str(self.title)


class UrTube:
    users = []
    videos = []

    def __init__(self):
        self.current_user = None

    def register(self, nickname, password, age):
        new_account = User(nickname, password, age)
        for i in self.users:
            if new_account.nickname == i.nickname:
                print('Пользователь ', i.nickname, ' уже существует')
                return self
        self.users.append(new_account)
        self.current_user = new_account
        return self

    def login(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                break
            else:
                print('Пользователя с данным паролем не существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            check_video = False
            for j in self.videos:
                if i == j:
                    check_video = True
                    break
            if check_video is False:
                self.videos.append(i)
        return self

    def get_videos(self, find_string):
        my_list = []
        for video in self.videos:
            if find_string.lower() in str(video.title).lower():
                my_list.append(video.title)
        return my_list

    def watch_video(self, name_video):
        import time
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        if self.get_videos(name_video) == []:
            print('Видео не существует')
            return
        for i in self.videos:
            if name_video == i.title:
                if i.adult_mode and self.current_user.age < 18:
                    print("Вам нельзя, вы маленький")
                    return None
                for j in range(i.duration):
                    i.time_now += 1
                    print(i.time_now, end=' ')
                    time.sleep(1)
                print('Конец видео')
                i.time_now = 0


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
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
