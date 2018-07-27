<?php
namespace Home\Controller;
use Think\Controller;
class HouseController extends Controller {
    public function detail($id){
    	$House = M("ershou");
		$house = $House->where("id=$id")->find();

		$condition['house_id']=$id;
		$Subway = M("subway");
		$subways = $Subway->where($condition)->select();

		$Bus = M("bus");
		$buses = $Bus->where($condition)->select();

		$School = M("school");
		$schools = $School->where($condition)->select();

		$Hospital = M("hospital");
		$hospitals = $Hospital->where($condition)->select();	

		$Work = M("work");
		$works = $Work->where($condition)->select();	

		$Shop = M("shop");
		$shops = $Shop->where($condition)->select();

		
		$distances = array();

		$total = 0;
		$num = count($subways);
		for($i=0;$i<$num;++$i){ 
			
			$total+= $subways[$i]['distance'];
		}
		$distances[0] = $num==0?0:$total*1.0/$num;

		$total = 0;
		$num = count($buses);
		for($i=0;$i<$num;++$i){ 
			
			$total+= $buses[$i]['distance'];
		} 
		$distances[1] = $num==0?0:$total*1.0/$num;

		$total = 0;
		$num = count($schools);
		for($i=0;$i<$num;++$i){ 
			
			$total+= $schools[$i]['distance'];
		} 
		$distances[2] = $num==0?0:$total*1.0/$num;

		$total = 0;
		$num = count($hospitals);
		for($i=0;$i<$num;++$i){ 
			
			$total+= $hospitals[$i]['distance'];
		} 
		$distances[3] = $num==0?0:$total*1.0/$num;

		$total = 0;
		$num = count($works);
		for($i=0;$i<$num;++$i){ 
			
			$total+= $works[$i]['distance'];
		} 
		$distances[4] = $num==0?0:$total*1.0/$num;

		$total = 0;
		$num = count($shops);
		for($i=0;$i<$num;++$i){ 
			
			$total+= $shops[$i]['distance'];
		} 
		$distances[5] = $num==0?0:$total*1.0/$num;


		$this->assign("house",$house);
		$this->assign('subways',$subways);
		$this->assign('buses',$buses);
		$this->assign('schools',$schools);
		$this->assign('hospitals',$hospitals);
		$this->assign('works',$works);
		$this->assign('shops',$shops);
		$this->assign('shops',$shops);
		$this->assign('distances',$distances);
		$this->display();
    }
}