var app = angular.module('pistrion-app', [
    'ngResource'
]);


app.config(function($interpolateProvider) {

    $interpolateProvider.startSymbol("{$");
    $interpolateProvider.endSymbol("$}");
    
});


app.controller('AppController', function($scope, $resource, Song) {
    var nums = [];
    while(nums.length < 4) {
        var ranNum=Math.floor((Math.random()*101) + 1);
        var found=false;
        for(var i=0; i<nums.length;i++){
            if(nums[i]==ranNum){found=true;break}
        }
        if(!found)nums[nums.length]=ranNum;
    }
    $scope.song1 = Song.get({id:nums[0]});
    $scope.song2 = Song.get({id:nums[1]});
    $scope.song3 = Song.get({id:nums[2]});
    $scope.song4 = Song.get({id:nums[3]});
    console.log($scope.song1);

    
});

app.factory('Song', function($resource) {
    return $resource('/api/songs/:id', {id:'@id'});
});
