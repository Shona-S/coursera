import unittest
from app.emotion_detector import emotion_predictor

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_output_format(self):
        result = emotion_predictor("I am thrilled to work on this project!")
        self.assertIsInstance(result, dict)
        self.assertIn("joy", result)

    def test_blank_input(self):
        with self.assertRaises(ValueError):
            emotion_predictor("")

if __name__ == "__main__":
    unittest.main()
