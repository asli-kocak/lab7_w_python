#version 330

#define PI 3.1415926535897932384626433832795

uniform mat4 myProjectionMatrix;
uniform mat4 myModelviewMatrix;
uniform mat4 myModelMatrix;
uniform vec3 myLightPos;
uniform sampler2D myTexture;
uniform sampler2D myNormalMap;

in vec3 myNormal;
in vec3 myPosition;

out vec3 normal;
out vec3 position;
out float u;
out float v;

out vec4 textCord;
out vec4 normalmap;

void main() {
	v = myPosition.y;
	u = atan(myPosition.z, myPosition.x) / 2 * PI;

	v = v * 1.5;
	u = u * 1.5;

	textCord = texture(myTexture, vec2(u,v));

	normalmap = texture(myNormalMap, vec2(u, v));
	normalmap.x = normalmap.x * 2.0 - 1.0;
	normalmap.y = normalmap.y * 2.0 - 1.0;
	normalmap.z = normalmap.z * 2.0 - 1.0;

	normal = myNormal;

    position = (myModelMatrix * vec4(myPosition, 1.0)).xyz;
    gl_Position = (myProjectionMatrix * myModelviewMatrix * vec4(myPosition, 1.0));
}

