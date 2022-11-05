def test_func()->str:
    print('Entered the test_func to test the internal class in a method definition')
    class InternalClass:
        def hello_world(self)->str:
            return "I'm inside the internal class."

    internal_class_obj = InternalClass()
    return internal_class_obj.hello_world()


print(test_func())
    