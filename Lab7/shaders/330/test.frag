#version 330

uniform vec3 myEyePos;
uniform vec3 myLightPos;
uniform sampler2D myTexture;
uniform sampler2D myNormalMap;

in vec3 normal;
in vec3 position;
in float u;
in float v;

in vec4 textCord;
in vec4 normalmap;

out vec4 outputColor; //this tells OpenGL that this variable is the output color

void main()
{
    vec3 light_dir = normalize(myLightPos - position);

    float diffuse_geo = dot(light_dir, normal);
	float diffuse_nm = dot(light_dir, normalmap.xyz);

	float diffuse = dot(diffuse_geo, diffuse_nm);

	outputColor = vec4(diffuse_geo * textCord.xyz, 1.0);
}
