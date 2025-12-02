import unittest
from math_blaster import MathEngine

class TestMathGame(unittest.TestCase):

    def setUp(self):
        """Executado antes de cada teste. Prepara o ambiente."""
        self.engine = MathEngine()

    def test_initial_state(self):
        """Verifica se o jogo começa com valores corretos."""
        self.assertEqual(self.engine.score, 0)
        self.assertEqual(self.engine.lives, 3)

    def test_check_answer_correct(self):
        """Testa se o sistema reconhece uma resposta correta."""
        # A resposta correta é 10 (int). O input é "10" (string).
        is_correct = self.engine.check_answer("10", 10)
        self.assertTrue(is_correct, "Deveria retornar True para resposta correta")

    def test_check_answer_wrong(self):
        """Testa se o sistema rejeita resposta errada."""
        is_correct = self.engine.check_answer("5", 10)
        self.assertFalse(is_correct, "Deveria retornar False para resposta errada")

    def test_check_answer_invalid_input(self):
        """Testa se o sistema lida com letras em vez de números."""
        is_correct = self.engine.check_answer("abc", 10)
        self.assertFalse(is_correct, "Deveria tratar input não numérico sem travar")

    def test_score_update(self):
        """Testa se a pontuação sobe corretamente."""
        self.engine.update_score(correct=True)
        self.assertEqual(self.engine.score, 10)
        
        self.engine.update_score(correct=True)
        self.assertEqual(self.engine.score, 20)

    def test_lose_life(self):
        """Testa a mecânica de perder vidas e Game Over."""
        # Perde 1 vida (restam 2)
        alive = self.engine.lose_life()
        self.assertEqual(self.engine.lives, 2)
        self.assertTrue(alive)

        # Perde +2 vidas (resta 0)
        self.engine.lose_life()
        alive = self.engine.lose_life()
        
        self.assertEqual(self.engine.lives, 0)
        self.assertFalse(alive, "O jogo deveria sinalizar Game Over (False)")

    def test_question_generation_format(self):
        """Verifica se o gerador retorna os tipos de dados esperados."""
        q_text, q_ans = self.engine.generate_question()
        self.assertIsInstance(q_text, str)
        self.assertIsInstance(q_ans, int)

if __name__ == '__main__':
    unittest.main()