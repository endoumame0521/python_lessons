# クラスを定義
class User:
    count = 0
    # コンストラクタ(特殊な関数)
    def __init__(self, name):
        User.count += 1
        # インスタンス変数
        self.name = name
    # インスタンスメソッド
    def say_hi(self):
        print("hi {0}" .format(self.name))

    # クラスメソッド
    @classmethod
    def show_info(cls):
        print("{0} instances" .format(cls.count))


# インスタンス変数をクラスから作る
tom = User("tom")
bob = User("bob")

# インスタンス変数を出力
print(tom.name)
print(bob.name)

# インスタンスメソッドを使用
tom.say_hi()
bob.say_hi()
User("Jonh").say_hi()

# クラスメソッドを使用
User.show_info()