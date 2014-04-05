var app = angular.module('pistrion-app', []);


app.controller('AppController', function($scope) {
var nums = []
while(nums.length < 4){
    var ranNum=Math.floor((Math.random()*101) + 1);
    var found=false;
    for(var i=0; i<nums.length;i++){
        if(nums[i]==ranNum){found=true;break}
        }
    if(!found)nums[nums.length]=ranNum;
}
    var Song = $resource('/api/songs/:id', {id:'@id'});
    var song1 = Song.get({id:nums[0]}, function() {
        song1.$save();
    });
    console.log(song1);
    var song2 = Song.get({id:nums[1]}, function() {
        song2.$save();
    });
    var song3 = Song.get({id:nums[2]}, function() {
        song3.$save();
    });
    var song4 = Song.get({id:nums[3]}, function() {
        song3.$save();
    });
});
