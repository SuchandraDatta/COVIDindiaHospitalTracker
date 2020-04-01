var app=angular.module("computer", ['ngRoute']);//gives error if there are no []
//injecting pages blocked by chrome, firefox if no server is setup but works so far in Edge
app.config(['$routeProvider', function($routeProvider){
    $routeProvider.when('/main', { templateUrl: 'main.html', controller: 'MainCtrl'});
}]).controller('MainCtrl', ['$scope', '$http', 
function($scope, $http){
    console.log('hello world from controller');
    $http.get('./dataFromScraping.json')
        .then( function(response)
                    {   console.log(response.data)
                        $scope.locInfo=response.data;

beds={
    "Maharashtra":"120444",
    "Kerala":"77515",
    "Karnataka":"126498",
    "Uttar Pradesh":"129729",
    "Telangana":"38341",
    "Gujarat":"73409",
    "Rajasthan":"83692",
    "Delhi":"44955",
    "Tamil Nadu":"150148",
    "Madhya Pradesh":"66979",
    "Jammu and Kashmir":"22993",
    "Punjab":"31460",
    "Haryana":"25081",
    "Andhra Pradesh":"83937",
    "West Bengal":"409317",
    "Ladakh":"-1",
    "Assam":"-1",
    "Himachal Pradesh":"-1",
    "Jharkhand":"-1",
    "Bihar":"29815",
    "Andaman and Nicobar Islands":"2321",
    "Chandigarh":"4534",
    "Chhattisgarh":"23766",
    "Uttarakhand":"129729",
    "Goa":"5679",
    "Odisha":"35016",
    "Manipur":"3989",
    "Mizoram":"4309",
    "Puducherry":"8031"
}
                        for(i=0;i<$scope.locInfo.length;i++)
                            {
                                //console.log($scope.locInfo[i].activeCases)
                                //console.log(beds[$scope.locInfo[i].state])
                                x=parseInt($scope.locInfo[i].activeCases)
                                y=parseInt(beds[$scope.locInfo[i].state])
                                console.log(y)
                                diff=y-x
                                if(y==-1)
                                {
                                    console.log("No info available")
                                    $scope.locInfo[i].activeCases="No info avaliable"
                                }
                                else
                                $scope.locInfo[i].activeCases=y-x
                                console.log((y-x))
                            }
                    }
            )
}])