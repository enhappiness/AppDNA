var Model = (function(){

  return {
    filters:{
      "score":function(item1,item2){
        return item.score > item.score;
      }
    },  
    fetchDNA : function(){
      return DNA_Pool; 
    }
  };
})();


var AppFinder = (function(window,document,undefined){
  
  var slice = [].slice,
      Model = window.Model;

  function flattern(arrs){
    return arrs.length > 0 ?
      [].concat.apply([],arrs) : arrs;
  }
  function elimateDuplicates(arr){
    var i , 
        len = arr.length,
        pack = {},
        result = [];
    for(i = 0; i< len ;i++){
      pack[arr[i]] = 1;
    }
    if(pack.length == len){
      return arr;
    }
    else{
      for( i in pack){
        result.push(i);
      }
    }
    return result;
  }

  //combine feature 
  function generateDNA(str){
    return str.split("+");
  }
  

  function mix(){
    var args = slice.call(arguments,0),
        flatternArr = flattern(args).sort();
  }
  function addfilter(apps,filters){
    filters.forEach(function(val,idx){
      apps = apps.filter(val)
    }); 
    return apps;
  }

  function fetchPool(features,filter){
    var DNA_Pool  = Model.fetchDNA(),
        result = [],
        tempItem;
    
    features.forEach(function(item,idx){
      tempItem = DNA_Pool[item]; 
      tempItem && result.push(tempItem);
    });

    filter && (result = filter(result));
    return elimateDuplicates(flattern(result));
  }

  function showApps(pool){
  }

  return {
    showApps:showApps,
    fetchPool:fetchPool,
    addfilter:addfilter,
    generateDNA:generateDNA
  }

})(window,document);
