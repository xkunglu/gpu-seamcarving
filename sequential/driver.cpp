//
// 18645 - GPU Seamcarving
// Authors: Adu Bhandaru, Matt Sarett
// modified: Xkunglu
//

#include "driver.h"
using namespace std;

using std::cout;
using std::endl;


int main(int argc, char const *argv[]) {

  for (int i = 0; i < argc; ++i) {
    std::cout << i << argv[i] << std::endl;
  }


  // Parse args
  if (argc < 3) {
    cout << "Usage: driver.out -n $num_seams [-i $image_name [-o $image_name]" << endl;
    exit(1);
  }

  string img_file = "";
  string out_file = "";
  img_file = (argc >= 5) ? argv[4] : "../images/boat-1024.bmp";
  out_file = (argc >= 7) ? argv[6] : "../outputs/sequential.bmp";

  // Load a bitmap image.
  Image image(img_file.c_str());

  // Simple test to see if the image was loaded correctly.
  cout << ">> pixel (0, 1): " << endl;
  const RGBQuad& p = image[0][1];
  cout << "   R: " << (int)p.red << endl;
  cout << "   G: " << (int)p.green << endl;
  cout << "   B: " << (int)p.blue << endl;

  // Clock start time.
  int num_seams = atoi(argv[2]);
  cout << ">> init seamcarver" << endl;
  cout << "   removing " << num_seams << " seams ..." << endl;
  clock_t begin = clock();

  // Remove seams.
  Seamcarver seamcarver(&image);
  seamcarver.removeSeams(num_seams);

  // Clock end time.
  clock_t end = clock();
  clock_t exec_time = end - begin;
  cout << ">> Execution time ..." << endl;
  cout << "   cycles: " << exec_time << endl;
  cout << "   time: " << ((double)exec_time /  CLOCKS_PER_SEC) << "s" << endl;
  cout << "   out file: " << out_file << endl;

  // Clean up and return normally.
  image.save(out_file.c_str());
  return 0;
}
