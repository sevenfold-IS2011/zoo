<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
		<h3>Animals descriptions:</h3>
			<xsl:for-each select="zoo:area">
			<xsl:if test="@id=">
				<h4><xsl:value-of select="./@name"/> list:</h4>
					<xsl:for-each select="zoo:animal">
						<p> -- Name: <xsl:value-of select="zoo:name"/></p>
						<p>Gender: <xsl:value-of select="zoo:gender"/></p>
						<p>Age: <xsl:value-of select="zoo:age"/></p>
						<p>photo:
			  			<img>
      	  			<xsl:attribute name="src">
            			<xsl:value-of select="zoo:img" />
        				</xsl:attribute>
    					</img>
						</p>
					</xsl:for-each>
			</xsl:if>
			</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>

