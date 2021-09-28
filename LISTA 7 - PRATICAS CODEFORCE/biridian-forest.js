function toInt(v){ return parseInt(v); }
function str(c, n){
	var ret = [];
	while(n--){
		ret.push(c);
	}
	return ret;
}
var _l = readline().split(' ');
var r = +_l[0] + 1;
var c = +_l[1] + 1;
 
var m = [];
 
m.push( str("T", c+1) );
for(var i=1; i<r; i++){
	m.push( ("T"+readline()+"T").split('') );
}
m.push( str("T", c+1) );
var start,end;
for(var i=1; i<r; i++){
	for(var j=1; j<c; j++){
		if(m[i][j]==='S'){
			start = [i,j];
			m[i][j] = '0';
		}else if(m[i][j]==='E'){
			end = [i,j];
			m[i][j] = '0';
		}
	}
}
 
 
var x = [1,-1,0,0];
var y = [0,0,1,-1];
var q = [end];
var i = 0;
var ret = 0;
while(i<q.length){
	var flg = false;
	for(var l=q.length; i<l; i++){
		var v = q[i];
		if( v[0]===start[0]&&v[1]===start[1]){
			flg = true;
		}else if(m[v[0]][v[1]]=='T'){
			continue;
		}else{
			ret += (parseInt( m[v[0]][v[1]] ));
		}
 
		m[v[0]][v[1]]='T';
		for(_i=0; _i<4; _i++){
			var xx = v[0] + x[_i];
			var yy = v[1] + y[_i];
			if(m[xx][yy]!=='T'){
				q.push([xx, yy]);
			}
		}
	}
	if(flg){
		break;
	}
}
print(ret);