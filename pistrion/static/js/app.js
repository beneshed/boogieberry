var nums = []
while(nums.length < 4){
    var ranNum=Math.floor((Math.random()*101) + 1);
    var found=false;
    for(var i=0; i<arr.length;i++){
        if(arr[i]==ranNum){found=true;break}
        }
    if(!found)arr[arr.length]=ranNum

app = angular.module 'pistirion', ['ngResource']

    var Song = $resource('/api/songs/:id', {id:'@id'});
    var song1 = Song.get({id:found[0]}, function() {
    });
    var song2 = Song.get({id:found[1]}, function() {
    });
    var song3 = Song.get({id:found[2]}, function() {
    });
    var song4 = Song.get({id:found[3]}, function() {
    });
