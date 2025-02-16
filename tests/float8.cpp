/*
   Copyright 2018 - The OPRECOMP Project Consortium, Universitat Jaume I,
                    IBM Research GmbH. All rights reserved.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/

#include <gtest/gtest.h>
#include <float.hpp>
#include <sstream>
#include <vector>
#include "float8_test_data.hpp"

using namespace NT_Float;
using namespace TEST_FP8_DATA;

namespace {

TEST(Floatx8RandomBitTest, ResultHasCorrectType)
{
    std::stringstream ss;
    for (size_t i = 0; i < FP8_E4M3_INPUT.size(); i++) {
        auto output = float8_e4m3(FP8_E4M3_INPUT[i]);
        ss << output;
        EXPECT_TRUE(ss.str() == FP8_E4M3_GOLDEN[i]);
        ss.str("");
    }
}


}  // namespace
