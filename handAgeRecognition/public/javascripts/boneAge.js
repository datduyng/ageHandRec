var app = angular.module('boneAge', ['ngResource','ngRoute']);

app.config(['$routeProvider', function($routeProvider){
    $routeProvider
        .when('/', {
            templateUrl: 'partials/homePage.html',
            controller: 'HomePageCtrl'
        })
        .otherwise({    
            redirectTo: '/'
        });
}]);

app.controller('HomePageCtrl', ['$scope', '$resource', '$location', '$routeParams', '$route',
    function($scope, $resource, $location, $routeParams, $route){

        $scope.submit = function(){
            var formData = new FormData($('#uploadFile')[0]);
            console.log(formData)
            $.ajax({
                    url : '/upload',
                    type : 'POST',
                    data : formData,
                    processData: false,
                    contentType: false,
                    cache : false,
                    success : function(data) {

                        console.log(data.error);
                        if(data.error == 1){
                            alert("Please select a file to upload. ");
                        } else {
                            alert("Upload successful!! Generating " + data.result + "...");
                        }
                    }
                });

        };
}]);


