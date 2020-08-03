import unittest
import aws_rekognition

class RekognitionTestCase(unittest.TestCase):

    def test_detect_faces(self):
        photo = 'a_girl.png'
        bucket = 'edwin456'
        response = aws_rekognition.detect_faces(photo, bucket)
        for face_detail in response['FaceDetails']:
            if face_detail['Gender']['Value'] == 'Female':
               print()
               print('Gender: Female')
               print('Confidence: {}'.format(face_detail['Gender']['Confidence']))
               result = True
            else:
               result = False
        self.assertEqual(result, True)

    def test_detect_labels(self):
        photo = 'photo.jpg'
        bucket = 'edwin456'
        response = aws_rekognition.detect_labels(photo, bucket)
        for lable in response['Labels']:
            if lable['Name'] == 'Family':
               result = True
               print()
               print('This picture is about a family.')
               print('Confidence: {}'.format(lable['Confidence']))
        self.assertEqual(result, True)

    def test_compare_faces(self):
        source_img = 'keiko1.jpg'
        target_img = 'keiko2.jpg'
        bucket = 'edwin456'
        response = aws_rekognition.compare_faces(source_img, target_img, bucket)
        for face_match in response['FaceMatches']:
            if face_match['Similarity'] > 90.0:
               result = True
               print()
               print('Similarity: {}'.format(face_match['Similarity']))
        self.assertEqual(result, True)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(RekognitionTestCase('test_detect_faces'))
    suite.addTest(RekognitionTestCase('test_detect_labels'))
    suite.addTest(RekognitionTestCase('test_compare_faces'))
    unittest.main(verbosity=2)