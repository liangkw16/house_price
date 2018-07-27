<?php
namespace Home\Controller;
use Think\Controller;
class ShopController extends Controller {
    public function index($id){
		$condition['house_id']=$id;
		$Shop = M("shop");
		$shops = $Shop->where($condition)->select();
		$this->ajaxReturn($shops,'JSON');
    }
}