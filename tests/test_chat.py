from zhipuai import ZhipuAI


def test_completions():
    client = ZhipuAI()  # 填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
            {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的slogan"},
            {"role": "assistant", "content": "当然，为了创作一个吸引人的slogan，请告诉我一些关于您产品的信息"},
            {"role": "user", "content": "智谱AI开放平台"},
            {"role": "assistant", "content": "智启未来，谱绘无限一智谱AI，让创新触手可及!"},
            {"role": "user", "content": "创造一个更精准、吸引人的slogan"}
        ],
        extra_body={"temperature": 0.5, "max_tokens": 50},
    )
    print(response.choices[0].message)


def test_completions_vis():
    client = ZhipuAI()  # 填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-4v",  # 填写需要调用的模型名称
        extra_body={"temperature": 0.5, "max_tokens": 2},
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "图里有什么"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://img1.baidu.com/it/u=1369931113,3388870256&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1703696400&t=f3028c7a1dca43a080aeb8239f09cc2f"
                        }
                    }
                ]
            }
        ]
    )
    print(response.choices[0].message)


if __name__ == "__main__":
    test_completions_vis()
