import unittest
from unittest.mock import Mock
from limit.limit_order_agent import LimitOrderAgent

class Test_Limit_Order_Agent(unittest.TestCase):

    def test_buy_order(self):
    
        exec_client = Mock()
        agent = LimitOrderAgent(exec_client)
        
        # Buy order for IBM
        agent.add_order(buy=True,product_id="IBM",
        amount=1000,price_limit=100)
        
        #Price is above the limit,order should not execute
        agent.on_price_tick(product_id="IBM", price=105)
        self.assertFalse(execution_client.buy.called)

        #Price is below the limit,order should execute
        agent.on_price_tick(product_id="IBM",price=99)
        self.assertTrue(execution_client.buy.called)
        self.assertEqual(execution_client.buy.call_args,
        (("IBM", 1000),))
        
    def test_sell_order(self):
        execution_client = Mock()
        agent = LimitOrderAgent(execution_client)

        # Add a sell order for AAPL
        agent.add_order(buy=False,product_id="AAPL",
        amount=500,price_limit=150)

        #Price is below the limit,order should not execute
        agent.on_price_tick(product_id="AAPL",price=140)
        self.assertFalse(execution_client.sell.called)

        #Price is above the limit, order should execute
        agent.on_price_tick(product_id="AAPL",price=151)
        self.assertTrue(execution_client.sell.called)
        self.assertEqual(execution_client.sell.call_args,
        (("AAPL", 500),))
        
        
if __name__ == '__main__':
    unittest.main()