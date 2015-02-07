angular.module("todoApp", [])
    /*
    The controller works behind the scenes to power your view.
    
    $scope is an angular service that maps elements from the 
    controller code to DOM elements in your view.
    
    The array argument allows for dependency injection. in both the
    module and the controller.
    */
    .controller("TodoController", ["$scope", function ($scope) {
        /*
        Todos is being added to the scope of the controller.
        Now it is a model in our angular app and we can store data
        in the model that will automatically update the view.
        
        $scope is a service of Angular that is being injected into
        the controller.
        */
        $scope.todos = [
            {text: "learn angular", done: true},
            {text: "build an angular app", done: false}
        ];
        /*
        This function can now be invoked by DOM elements to
        interact with a model.
        */
        $scope.addTodo = function () {
            $scope.todos.push({text: $scope.todoText, done: false});
            $scope.todoText = "";
        };
        /*
        This is a computed property.  Its value can be assigned to
        DOM elements in the view.
        */
        $scope.remaining = function () {
            var count = 0;
            angular.forEach($scope.todos, function (todo) {
                count += todo.done ? 0 : 1;    
            });
            return count;
        };
        /*
        This function adds objects to the model
        */
        $scope.archive = function () {
            var oldTodos = $scope.todos;
            $scope.todos = [];
            angular.forEach(oldTodos, function (todo) {
                if (!todo.done) {
                    $scope.todos.push(todo);
                }
            });
        };
    }]);